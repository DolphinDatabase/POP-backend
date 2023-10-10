from database import SessionLocal
from model import Usuario,Historico
from schema import CreateUsuario,UsuarioBase,CreateHistorico
from .historico_service import HistoricoService
from .termo_service import TermoService
import crypt

class UsuarioService:
    def create_usuario(usuario:CreateUsuario):
        u = Usuario(nome = usuario.nome,
                    doc = usuario.doc,
                    proprietario = usuario.proprietario,
                    email = usuario.email,
                    senha = crypt.hash_password(usuario.senha),
                    permissao = True)
        db = SessionLocal()
        db.add(u)
        db.commit()
        db.refresh(u)
        db.close()
        t = TermoService.get_last(usuario.proprietario)
        HistoricoService.create_historico(CreateHistorico(usuario=u.id,termo=t.id))
        return u

    def get_usuario(id:int):
        db = SessionLocal()
        u = db.query(Usuario).where(Usuario.id == id).first()
        if u is None:
            raise Exception(404, 'Usuario not found')
        return u
    
    def get_usuario_by_email(email: str) -> Usuario:
        db = SessionLocal()
        usuario = db.query(Usuario).where(Usuario.email == email).first()
        return usuario

    def usuario_sign(id:int):
        db = SessionLocal()
        u = db.query(Usuario).where(Usuario.id == id).first()
        if u is None:
            db.close()
            raise Exception(404, 'Usuario not found')
        if u.permissao:
            db.close()
            raise Exception(401,'Usuario already sign')
        t = TermoService.get_last(u.proprietario)
        HistoricoService.create_historico(CreateHistorico(usuario=u.id,termo=t.id))
        u.permissao = True
        db.add(u)
        db.commit()
        db.refresh(u)
        db.close()
        return u
        

    def update_usuario(id:int, usuario:UsuarioBase):
        db = SessionLocal()
        u = db.query(Usuario).where(Usuario.id==id).first()
        if u is None:
            db.close()
            raise Exception(404, 'Usuario not found')
        u.nome = usuario.nome
        u.doc = usuario.doc
        u.email = usuario.email
        db.add(u)
        db.commit()
        db.refresh(u)
        db.close()
        return u
        
    def delete_usuario(id:int):
        db = SessionLocal()
        u = db.query(Usuario).where(Usuario.id==id).first()
        if u is None:
            db.close()
            raise Exception(404, 'Usuario not found')
        db.delete(u)
        db.commit()
        db.close()

