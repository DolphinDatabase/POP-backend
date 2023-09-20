from database import SessionLocal
from model.gleba import Gleba
from schema.schemas import Gleba as GlebaBase
from geoalchemy2.functions import ST_AsGeoJSON
import json


def get_glebas(skip: int = 0, limit: int = 100):
    with SessionLocal() as db:
        glebas = db.query(Gleba).offset(skip).limit(limit).all()
    return glebas

def get_gleba(id: int):
    with SessionLocal() as db:
        gleba = db.query(Gleba).filter(Gleba.id == id).first()
        if gleba is None:
            raise Exception()
    return gleba