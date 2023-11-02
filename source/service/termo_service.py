from database import SessionLocal
from model import Termo,Usuario
from schema import TermoBase
from datetime import date


class TermoService:
    @staticmethod
    def create_termo(termo: TermoBase):
        t = Termo(data=date.today(), proprietario=termo.proprietario,
                text=termo.text)
        db = SessionLocal()
        db.add(t)
        db.query(Usuario).filter(Usuario.proprietario == termo.proprietario).update({Usuario.permissao:False})
        db.commit()
        db.refresh(t)
        db.close()
        return t

    @staticmethod
    def index_termo():
        db = SessionLocal()
        termos = db.query(Termo).all()
        db.close()
        return termos

    @staticmethod
    def get_termo(id: int):
        db = SessionLocal()
        termo = db.query(Termo).where(Termo.id == id).first()
        db.close()
        if termo is None:
            raise Exception(404, 'Termo not found')
        return termo

    @staticmethod
    def get_last(prop: bool):
        db = SessionLocal()
        termo = db.query(Termo).where(Termo.proprietario == prop).order_by(Termo.id.desc()).first()
        db.close()
        if termo is None:
            raise Exception(404, 'Termo not found')
        return termo

    @staticmethod
    def update_termo(id: int, termo: TermoBase):
        db = SessionLocal()
        t = db.query(Termo).where(Termo.id == id).first()
        if t is None:
            db.close()
            raise Exception(404, 'Termo not found')
        t.text = termo.text
        t.proprietario = termo.proprietario
        t.data = date.today()
        db.add(t)
        db.commit()
        db.refresh(t)
        db.close()
        return t

    @staticmethod
    def delete_termo(id: int):
        db = SessionLocal()
        t = db.query(Termo).where(Termo.id == id).first()
        if t is None:
            db.close()
            raise Exception()
        db.delete(t)
        db.commit()
        db.close()
