from copy import copy, deepcopy

from controller.exceptions import registration_exception, object_not_found_exception
from database import SessionLocal
from model import Usuario, Grupo
from schema import CreateUsuario, BaseUsuario, UpdateUsuario
import crypt
import cache
import database


class UsuarioService:
    @staticmethod
    def get_users_keys() -> dict:
        sqlite_cursor = database.sqlite_conn.cursor()
        res = sqlite_cursor.execute("SELECT * FROM users")
        user_keys = res.fetchall()
        return {id: key for (id, key) in user_keys}

    def encrypt_user(self, usuario: Usuario) -> Usuario:
        key = self.get_users_keys()[usuario.id]
        usuario.email = crypt.encrypt_data(usuario.email, key)
        usuario.nome = crypt.encrypt_data(usuario.nome, key)
        usuario.doc = crypt.encrypt_data(usuario.doc, key)
        return usuario

    def decrypt_user(self, usuario: Usuario) -> Usuario:
        key = self.get_users_keys()[usuario.id]
        decrypted_user = deepcopy(usuario)
        decrypted_user.email = crypt.decrypt_data(usuario.email, key)
        decrypted_user.nome = crypt.decrypt_data(usuario.nome, key)
        decrypted_user.doc = crypt.decrypt_data(usuario.doc, key)
        return decrypted_user

    def init_cache(self) -> None:
        sqlite_cursor = database.sqlite_conn.cursor()
        sqlite_cursor.execute("CREATE TABLE IF NOT EXISTS users(id, key)")
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
    def get_usuario_by_email(email: str):
        usuario_dict = cache.get_object(f"user:{email}")

        if not usuario_dict:
            return None
        else:
            return Usuario.from_dict(usuario_dict)

    def create_usuario(self, novo_usuario: CreateUsuario) -> Usuario:
        usuario = self.get_usuario_by_email(novo_usuario.email)

        if usuario is not None and usuario.ativo:
            raise registration_exception

        usuario = Usuario()
        usuario.nome = novo_usuario.nome
        usuario.doc = novo_usuario.doc
        usuario.email = novo_usuario.email
        usuario.senha = crypt.hash_password(novo_usuario.senha)
        usuario.grupo = novo_usuario.grupo.value
        usuario.ativo = False

        cache.add_object(f"user:{usuario.email}", usuario.as_dict())

        if usuario.grupo == Grupo.ADMINISTRADOR.value:
            return self.active_user(usuario)

        return usuario

    def active_user(self, usuario: Usuario):
        usuario = self.get_usuario_by_email(usuario.email)

        if usuario is None:
            return

        usuario.ativo = True

        with SessionLocal() as db:
            usuario_base = Usuario()
            usuario_base.senha = usuario.senha
            usuario_base.grupo = usuario.grupo
            usuario_base.ativo = usuario.ativo

            db.add(usuario_base)
            db.commit()
            db.refresh(usuario_base)

            usuario_base.email = usuario.email
            usuario_base.nome = usuario.nome
            usuario_base.doc = usuario.doc

            key = crypt.generate_random_key()
            database.sqlite_conn.execute(f"INSERT INTO users VALUES ({usuario_base.id}, '{key}')")
            database.sqlite_conn.commit()

            cache.add_object(f"user:{usuario_base.email}", usuario_base.as_dict())

            self.encrypt_user(usuario_base)

            db.add(usuario_base)
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

        database.sqlite_conn.execute(f"DELETE FROM users WHERE id = '{usuario.id}'")
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
            usuario_base = db.query(Usuario).where(Usuario.id == usuario.id).first()
            usuario_base.senha = usuario.senha
            usuario_base.email = usuario.email
            usuario_base.nome = usuario.nome
            usuario_base.doc = usuario.doc

            self.encrypt_user(usuario_base)

            db.add(usuario_base)
            db.commit()

        return usuario
