from ast import List, Tuple
from typing import Optional
from pydantic import BaseModel


class Propriedade(BaseModel):
    operacao_id: int

    class Config:
        orm_mode = True


class Operacao(BaseModel):
    inicio_plantio: str
    fim_plantio: str
    inicio_colheita: str
    fim_colheita: str
    estado: str
    municipio: str

    solo_id: int
    irrigacao_id: int
    cultivo_id: int
    grao_semente_id: int
    ciclo_id: int
    gleba_id: int
    empreendimento_id: int

    propriedades: list[Propriedade] = []

    class Config:
        orm_mode = True


class Solo(BaseModel):
    class Config:
        orm_mode = True


class Irrigacao(BaseModel):
    class Config:
        orm_mode = True


class Cultivo(BaseModel):
    class Config:
        orm_mode = True


class GraoSemente(BaseModel):
    class Config:
        orm_mode = True


class Ciclo(BaseModel):

    class Config:
        orm_mode = True

class Geometry(BaseModel):
    type: str
    coordinates: list[list[tuple[float,float]]]

class Feature(BaseModel):
    type: str
    geometry: Geometry

class Gleba(BaseModel):
    id:int
    poligono: Feature
    class Config:
        orm_mode = True


class Empreendimento(BaseModel):

    operacoes: list[Operacao] = []

    class Config:
        orm_mode = True
