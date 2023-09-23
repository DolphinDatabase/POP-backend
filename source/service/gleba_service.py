from database import SessionLocal
from model import Gleba,Operacao,Estado
from geoalchemy2.functions import ST_MakePoint,ST_SetSRID,ST_Distance

def get_glebas(skip: int = 0, limit: int = 100):
    with SessionLocal() as db:
        glebas = db.query(Gleba).offset(skip).limit(limit).all()
        features = []
        for glb in glebas:
            feature = glb.poligono
            feature['properties'] = {
                'gleba_id':glb.id,
                'operacao_id':glb.operacao_id     
            }
            features.append(feature)
    return {'type':'FeatureCollection','features':features}

def get_gleba(id: int):
    with SessionLocal() as db:
        gleba = db.query(Gleba).filter(Gleba.id == id).first()
        if gleba is None:
            raise Exception()
        feature = gleba.poligono
        feature['properties'] = {
            'gleba_id':gleba.id,
            'operacao_id':gleba.operacao_id     
        }
    return feature

def get_gleba_by_estado(sigla: str,skip:int=0,limit:int=100):
    with SessionLocal() as db:
        glebas = db.query(Gleba).join(Operacao).join(Estado).filter(Estado.descricao == sigla).offset(skip).limit(limit).all()
        features = []
        for glb in glebas:
            feature = glb.poligono
            feature['properties'] = {
                'gleba_id':glb.id,
                'operacao_id':glb.operacao_id     
            }
            features.append(feature)
    return {'type':'FeatureCollection','features':features}

def get_gleba_by_location(lat:float,long:float):
    with SessionLocal() as db:
        point = ST_SetSRID(ST_MakePoint(long, lat), 4326)
        glebas = db.query(
            Gleba
        ).order_by(ST_Distance(Gleba._poligono, point)).limit(100)
        features = []
        for glb in glebas:
            feature = glb.poligono
            feature['properties'] = {
                'gleba_id':glb.id,
                'operacao_id':glb.operacao_id     
            }
            features.append(feature)
    return {'type':'FeatureCollection','features':features}