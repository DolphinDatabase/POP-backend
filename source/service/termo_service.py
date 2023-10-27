from database import SessionLocal
from model import Termo, Usuario, Grupo, Condicao
from schema import TermoBase
from datetime import datetime
from sqlalchemy import func


class TermoService:
    @staticmethod
    def create_termo(novo_termo: TermoBase):
        with SessionLocal() as db:
            grupo = db.query(Grupo).filter(novo_termo.grupo == Grupo.descricao).first()

            termo = Termo(data=datetime.now(),
                          grupo_id=grupo.id,
                          texto=novo_termo.texto)

            for condicao in novo_termo.condicoes:
                condicao = Condicao(texto=condicao.texto)
                termo.condicoes.append(condicao)

            db.add(termo)
            db.commit()
            db.refresh(termo)

        termo.grupo = termo.grupo.descricao

        return termo

    @staticmethod
    def index_termo():
        with SessionLocal() as db:
            termos = db.query(Termo).all()

            for termo in termos:
                termo.grupo = termo.grupo.descricao

        return termos

    @staticmethod
    def get_termo(id: int):
        with SessionLocal() as db:
            termo = db.query(Termo).where(Termo.id == id).first()

        if termo is None:
            raise Exception(404, 'Termo not found')

        termo.grupo = termo.grupo.descricao

        return termo

    @staticmethod
    def get_last(usuario: Usuario):
        with SessionLocal() as db:
            termo = db.query(Termo, func.max(Termo.data)).where(Termo.grupo == usuario.grupo)

        if termo is None:
            raise Exception(404, 'Termo not found')

        return termo

    @staticmethod
    def update_termo(id: int, novo_termo: TermoBase):
        with SessionLocal() as db:
            termo = db.query(Termo).where(Termo.id == id).first()
            if termo is None:
                db.close()
                raise Exception(404, 'Termo not found')
            termo.texto = novo_termo.text
            termo.proprietario = novo_termo.proprietario
            termo.data = datetime.now()
            db.add(termo)
            db.commit()
            db.refresh(termo)

        return termo

    @staticmethod
    def delete_termo(id: int):
        with SessionLocal() as db:
            termo = db.query(Termo).where(Termo.id == id).first()
            if termo is None:
                db.close()
                raise Exception()
            db.delete(termo)
            db.commit()
