from pydantic import BaseModel
from model import Grupo


class UsuarioBase(BaseModel):
    nome: str
    doc: str
    email: str
    grupo: Grupo

    class Config:
        orm_mode = True


class GetUsuario(UsuarioBase):
    id: int


class CreateUsuario(UsuarioBase):
    senha: str
