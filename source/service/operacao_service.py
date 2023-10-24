from database import SessionLocal
from model.operacao import Operacao


def get_operacaos(skip: int = 0, limit: int = 100):
    with SessionLocal() as db:
        return db.query(Operacao).offset(skip).limit(limit).all()


def get_operacao(id: int):
    with SessionLocal() as db:
        operacao = db.query(Operacao).filter(Operacao.id == id).first()
        if operacao is None:
            raise Exception()
        return operacao

