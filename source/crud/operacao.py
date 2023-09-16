from sqlalchemy.orm import Session
from model.operacao import Operacao


def get_operacaos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Operacao).offset(skip).limit(limit).all()

def get_operacao(db: Session, id: int):
    return db.query(Operacao).filter(Operacao.id == id).first()
