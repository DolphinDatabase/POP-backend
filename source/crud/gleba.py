from sqlalchemy.orm import Session
from model.gleba import Gleba


def get_glebas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Gleba).offset(skip).limit(limit).all()

def get_gleba(db: Session, id: int):
    return db.query(Gleba).filter(Gleba.id == id).first()

