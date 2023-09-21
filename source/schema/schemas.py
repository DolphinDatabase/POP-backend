from pydantic import BaseModel, datetime_parse
from datetime import date


class Estado(BaseModel):
    descricao: str


class Municipio(BaseModel):
    descricao: str


class Propriedade(BaseModel):
    operacao_id: int

    class Config:
        orm_mode = True


class Solo(BaseModel):
    descricao: str
    class Config:
        orm_mode = True


class Irrigacao(BaseModel):
    descricao: str
    class Config:
        orm_mode = True


class Cultivo(BaseModel):
    descricao: str
    class Config:
        orm_mode = True


class GraoSemente(BaseModel):
    descricao: str
    class Config:
        orm_mode = True


class Ciclo(BaseModel):
    descricao: str
    class Config:
        orm_mode = True


class Operacao(BaseModel):
    inicio_plantio: date
    fim_plantio: date
    inicio_colheita: date
    fim_colheita: date
    estado: Estado
    municipio: Municipio

    solo: Solo
    irrigacao: Irrigacao
    cultivo: Cultivo
    grao_semente: GraoSemente
    ciclo: Ciclo
    empreendimento_id: int

    propriedades: list[Propriedade] = []

    class Config:
        orm_mode = True


class Property(BaseModel):
    estado: Estado
    municipio: Municipio


class Geometry(BaseModel):
    type: str
    coordinates: list[list[tuple[float, float]]]


class Feature(BaseModel):
    type: str
    geometry: Geometry
    properties: Property


class Gleba(BaseModel):
    id: int
    poligono: Feature

    class Config:
        orm_mode = True


class Empreendimento(BaseModel):

    operacoes: list[Operacao] = []

    class Config:
        orm_mode = True
