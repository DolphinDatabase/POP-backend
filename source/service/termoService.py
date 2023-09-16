from database import SessionLocal
from model.termo import Termo
from schema.termoSchema import TermoBase
from datetime import date

def create_termo(termo:TermoBase):
    t = Termo(data=date.today(),proprietario = termo.proprietario,text=termo.text)
    db = SessionLocal()
    db.add(t)
    db.commit()
    db.refresh(t)
    db.close()
    return t

def index_termo():
    db = SessionLocal()
    termos = db.query(Termo).all()
    db.close()
    return termos

def get_termo(id:int):
    db = SessionLocal()
    termo = db.query(Termo).where(Termo.id==id).first()
    if termo is None:
        raise Exception()
    return termo

def get_last():
    db = SessionLocal()
    termo = db.query(Termo).order_by(Termo.data.desc()).first()
    if termo is None:
        raise Exception()
    return termo

def update_termo(id:int, termo:TermoBase):
    db = SessionLocal()
    t = db.query(Termo).where(Termo.id==id).first()
    if t is None:
        db.close()
        raise Exception()
    t.text = termo.text
    t.proprietario = termo.proprietario
    t.data = date.today()
    db.add(t)
    db.commit()
    db.refresh(t)
    db.close()
    return t
    
def delete_termo(id:int):
    db = SessionLocal()
    t = db.query(Termo).where(Termo.id==id).first()
    if t is None:
        db.close()
        raise Exception()
    db.delete(t)
    db.commit()
    db.close()