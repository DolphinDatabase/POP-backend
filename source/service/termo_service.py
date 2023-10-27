from database import SessionLocal
from model import Termo, Usuario, Grupo, Condicao
from schema import TermoBase
from datetime import datetime
from sqlalchemy import func


class TermoService:
    @staticmethod
    def create_termo(termo: TermoBase):
        with SessionLocal() as db:
            grupo_id = db.query(int).filter(termo.grupo == Grupo.descricao)

            termo_obj = Termo(data=datetime.now(),
                              grupo_id=grupo_id,
                              text=termo.text)

            for condicao in termo.terms:
                condicao = Condicao(texto=condicao.param)
                termo_obj.condicoes.append()

            db.add(termo_obj)
            db.commit()
            db.refresh(termo_obj)
        return termo_obj

    @staticmethod
    def index_termo():
        with SessionLocal() as db:
            termos = db.query(Termo).all()
        return termos

    @staticmethod
    def get_termo(id: int):
        with SessionLocal() as db:
            termo = db.query(Termo).where(Termo.id == id)

        if termo is None:
            raise Exception(404, 'Termo not found')
        return termo

    @staticmethod
    def get_last(usuario: Usuario):
        with SessionLocal() as db:
            termo = db.query(Termo, func.max(Termo.data)).where(Termo.grupo == usuario.grupo)

        if termo is None:
            raise Exception(404, 'Termo not found')
        return termo

    @staticmethod
    def update_termo(id: int, termo: TermoBase):
        with SessionLocal() as db:
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
        return t

    @staticmethod
    def delete_termo(id: int):
        with SessionLocal() as db:
            t = db.query(Termo).where(Termo.id == id).first()
            if t is None:
                db.close()
                raise Exception()
            db.delete(t)
            db.commit()
