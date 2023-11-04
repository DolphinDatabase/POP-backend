from pydantic import BaseModel
from datetime import datetime
from model import Servico
from typing import List, Optional

from model import Grupo, Servico


class BaseCondicao(BaseModel):
    texto: str
    servico: Optional[Servico] = None
    
class BaseTermo(BaseModel):
    texto: str
    grupo: Grupo
    condicoes: List[BaseCondicao]

    class Config:
        from_attributes = True


class GetCondicao(BaseCondicao):
    id: int


class GetTermo(BaseTermo):
    id: int
    data: datetime
    condicoes: List[GetCondicao]


class AcceptCondicao(GetCondicao):
    aceite: bool


class AcceptTermo(GetTermo):
    aceite: bool
    condicoes: List[AcceptCondicao]

    class Config:
        from_attributes = True
