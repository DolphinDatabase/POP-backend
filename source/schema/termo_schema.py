from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

from model import Grupo, Servico


class BaseCondicao(BaseModel):
    texto: str
    servico: str


class BaseTermo(BaseModel):
    texto: str
    grupo: Grupo
    condicoes: List[BaseCondicao]

    class Config:
        from_attributes = True


class GetCondicao(BaseModel):
    id: int
    texto: str


class GetTermo(BaseModel):
    id: int
    texto: str
    grupo: Grupo
    data: datetime
    condicoes: List[GetCondicao]


class AcceptCondicao(BaseModel):
    id: int
    aceite: bool


class AcceptTermo(BaseModel):
    id: int
    aceite: bool
    condicoes: List[AcceptCondicao]
