from typing import Optional

from pydantic import BaseModel
from model import Grupo


class BaseUsuario(BaseModel):
    nome: str
    doc: str
    email: str
    grupo: Grupo

    class Config:
        from_attributes = True


class GetUsuario(BaseUsuario):
    id: int


class CreateUsuario(BaseUsuario):
    senha: str


class UpdateUsuario(BaseModel):
    nome: Optional[str] = None
    doc: Optional[str] = None
    email: Optional[str] = None
    senha: Optional[str] = None
