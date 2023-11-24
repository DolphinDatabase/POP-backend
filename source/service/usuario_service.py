from copy import copy, deepcopy


from controller.exceptions import registration_exception, object_not_found_exception
from database import SessionLocal
from model import Usuario, Grupo
from schema import CreateUsuario, BaseUsuario, UpdateUsuario
import crypt
import cache
import database
import cache
import database


class UsuarioService:
    @staticmethod
    def get_users_keys() -> dict:
        sqlite_cursor = database.sqlite_conn.cursor()
        res = sqlite_cursor.execute("SELECT * FROM users")
        user_keys = res.fetchall()
        return {email: key for (email, key) in user_keys}

    def encrypt_user(self, usuario: Usuario) -> Usuario:
        key = self.get_users_keys()[usuario.email]
        encrypted_user = deepcopy(usuario)
        encrypted_user.email = crypt.encrypt_data(usuario.email, key)
        encrypted_user.nome = crypt.encrypt_data(usuario.nome, key)
        encrypted_user.doc = crypt.encrypt_data(usuario.doc, key)
        return encrypted_user

    def decrypt_user(self, usuario: Usuario) -> Usuario:
        key = self.get_users_keys()[usuario.email]
        decrypted_user = deepcopy(usuario)
        decrypted_user.email = crypt.decrypt_data(usuario.email, key)
        decrypted_user.nome = crypt.decrypt_data(usuario.nome, key)
        decrypted_user.doc = crypt.decrypt_data(usuario.doc, key)
        return decrypted_user

    def init_cache(self) -> None:
        sqlite_cursor = database.sqlite_conn.cursor()
        sqlite_cursor.execute("CREATE TABLE IF NOT EXISTS users(email, key)")
        sqlite_cursor.close()

        if cache.get_init():
            return

        with SessionLocal() as db:
            usuarios = db.query(Usuario).where(Usuario.ativo.is_(True))

        for usuario in usuarios:
            decrypted_user = self.decrypt_user(usuario)
            cache.add_object(f"user:{usuario.email}", decrypted_user.as_dict())

        cache.set_init()

    @staticmethod
    def get_usuario_by_email(email: str) -> Usuario:
        with SessionLocal() as db:
            usuario = db.query(Usuario).where(Usuario.email == email).first()
        return usuario

    @staticmethod
    def create_usuario(novo_usuario: CreateUsuario) -> Usuario:
        with SessionLocal() as db:
            usuario = (
                db.query(Usuario).where(Usuario.email == novo_usuario.email).first()
            )

            if usuario is None:
                usuario_is_admin = novo_usuario.grupo == Grupo.ADMINISTRADOR.value
                usuario = Usuario(ativo=usuario_is_admin)

            if usuario.ativo:
                raise registration_exception

            usuario.nome = novo_usuario.nome
            usuario.doc = novo_usuario.doc
            usuario.email = novo_usuario.email
            usuario.senha = crypt.hash_password(novo_usuario.senha)
            usuario.grupo = novo_usuario.grupo.value

            db.add(usuario)
            db.commit()

        return usuario

    def deactivate_user(self, usuario: Usuario):
        usuario = self.get_usuario_by_email(usuario.email)

        if usuario is None:
            return

        usuario.ativo = False
        cache.remove_object(f"user:{usuario.email}")

        with SessionLocal() as db:
            encrypted_usuario = self.encrypt_user(usuario)
            db.add(encrypted_usuario)
            db.commit()

        database.sqlite_conn.execute(f"DELETE FROM users WHERE email = '{usuario.email}'")
        database.sqlite_conn.commit()

        return usuario

    def update_usuario(self, novo_usuario: UpdateUsuario, usuario: Usuario) -> Usuario:
        usuario = self.get_usuario_by_email(usuario.email)

        if usuario is None:
            raise registration_exception

        if novo_usuario.nome is not None:
            usuario.nome = novo_usuario.nome

        if novo_usuario.doc is not None:
            usuario.doc = novo_usuario.doc

        if novo_usuario.email is not None:
            usuario.email = novo_usuario.email

        if novo_usuario.senha is not None:
            usuario.senha = crypt.hash_password(novo_usuario.senha)

        cache.add_object(f"user:{usuario.email}", usuario.as_dict())

        with SessionLocal() as db:
            encrypted_usuario = self.encrypt_user(usuario)
            db.add(encrypted_usuario)
            db.commit()

        return usuario

    @staticmethod
    def delete_usuario(usuario: Usuario) -> int:
        with SessionLocal() as db:
            usuario.nome = None
            usuario.doc = None
            usuario.email = None
            usuario.senha = None
            usuario.grupo = None
            usuario.ativo = False

            db.add(usuario)
            db.commit()
            db.refresh(usuario)

        return usuario.id
