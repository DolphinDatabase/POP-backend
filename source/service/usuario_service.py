from database import SessionLocal
from model.usuario import Usuario
from schema.usuarioSchema import UsuarioBase,CreateUsuario

def create_usuario(usuario:CreateUsuario):
    u = Usuario(nome = usuario.nome,
                doc = usuario.doc,
                proprietario = usuario.proprietario,
                email = usuario.email,
                senha = usuario.senha)
    db = SessionLocal()
    db.add(u)
    db.commit()
    db.refresh(u)
    db.close()
    return u

def get_usuario(id:int):
    db = SessionLocal()
    u = db.query(Usuario).where(Usuario.id == id).first()
    if u is None:
        raise Exception()
    return u

def update_usuario(id:int, usuario:UsuarioBase):
    db = SessionLocal()
    u = db.query(Usuario).where(Usuario.id==id).first()
    if u is None:
        db.close()
        raise Exception()
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
        raise Exception()
    db.delete(u)
    db.commit()
    db.close()

