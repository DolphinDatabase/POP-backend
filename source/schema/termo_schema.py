from pydantic import BaseModel
from datetime import datetime
from typing import List


class CondicaoBase(BaseModel):
    texto: str


class TermoBase(BaseModel):
    texto: str
    grupo: str
    condicoes: List[CondicaoBase]

    class Config:
        orm_mode = True


class GetCondicao(CondicaoBase):
    id: int


class GetTermo(TermoBase):
    id: int
    data: datetime
    condicoes: List[GetCondicao]
