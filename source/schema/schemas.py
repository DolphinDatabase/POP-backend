from pydantic import BaseModel
from datetime import date


class Estado(BaseModel):
    descricao: str


class Municipio(BaseModel):
    descricao: str


class Propriedade(BaseModel):
    operacao_id: int

    class Config:
        from_attributes = True


class Solo(BaseModel):
    descricao: str

    class Config:
        from_attributes = True


class Irrigacao(BaseModel):
    descricao: str

    class Config:
        from_attributes = True


class Cultivo(BaseModel):
    descricao: str

    class Config:
        from_attributes = True


class GraoSemente(BaseModel):
    descricao: str

    class Config:
        from_attributes = True


class Ciclo(BaseModel):
    descricao: str

    class Config:
        from_attributes = True


class Empreendimento(BaseModel):
    finalidade: str
    atividade: str
    modalidade: str
    produto: str
    variedade: str
    cesta: str
    zoneamento: str

    class Config:
        from_attributes = True


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
    empreendimento: Empreendimento

    propriedades: list[Propriedade] = []

    class Config:
        from_attributes = True


class Coordinates(BaseModel):
    coordinates: tuple[tuple[float, float]]


class Geometry(BaseModel):
    type: str
    coordinates: list[list[tuple[float, float]]]


class PolygonProperties(BaseModel):
    gleba_id: int
    operacao_id: int


class Feature(BaseModel):
    type: str
    geometry: Geometry
    properties: PolygonProperties


class FeatureCollections(BaseModel):
    type: str
    features: list[Feature]


class Gleba(BaseModel):
    id: int
    poligono: Feature

    class Config:
        from_attributes = True
