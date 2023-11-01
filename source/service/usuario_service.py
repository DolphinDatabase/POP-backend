from controller.exceptions import registration_exception, object_not_found_exception
from database import SessionLocal
from model import Usuario, Grupo
from schema import CreateUsuario, BaseUsuario
from .termo_service import TermoService
import crypt


class UsuarioService:
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
            db.refresh(usuario)

        return usuario

    @staticmethod
    def get_usuario_by_email(email: str) -> Usuario:
        with SessionLocal() as db:
            usuario = db.query(Usuario).where(Usuario.email == email).first()
        return usuario

    @staticmethod
    def update_usuario(novo_usuario: BaseUsuario) -> Usuario:
        with SessionLocal() as db:
            usuario = (
                db.query(Usuario).where(Usuario.email == novo_usuario.email).first()
            )

            if usuario is None:
                raise object_not_found_exception

            usuario.nome = novo_usuario.nome
            usuario.doc = novo_usuario.doc
            usuario.email = novo_usuario.email
            usuario.senha = crypt.hash_password(novo_usuario.senha)

            db.add(usuario)
            db.commit()
            db.refresh(usuario)

        return usuario

    @staticmethod
    def delete_usuario(usuario: Usuario) -> Usuario:
        with SessionLocal() as db:
            usuario = db.query(Usuario).where(Usuario.email == usuario.email).first()

            if usuario is None:
                raise object_not_found_exception

            db.delete(usuario)
            db.commit()

        return usuario

    @staticmethod
    def get_all():
        db = SessionLocal()
        u = db.query(Usuario.email).all()
        if u is None:
            raise Exception(404, "Table is empty")
        return u
