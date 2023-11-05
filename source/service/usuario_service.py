from controller.exceptions import registration_exception, object_not_found_exception
from database import SessionLocal
from model import Usuario, Grupo
from schema import CreateUsuario, BaseUsuario, UpdateUsuario
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
    def update_usuario(novo_usuario: UpdateUsuario, usuario: Usuario) -> Usuario:
        with SessionLocal() as db:
            if novo_usuario.nome is not None:
                usuario.nome = novo_usuario.nome

            if novo_usuario.doc is not None:
                usuario.doc = novo_usuario.doc

            if novo_usuario.email is not None:
                usuario.email = novo_usuario.email

            if novo_usuario.senha is not None:
                usuario.senha = crypt.hash_password(novo_usuario.senha)

            db.add(usuario)
            db.commit()
            db.refresh(usuario)

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
