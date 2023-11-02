from pydantic import BaseModel
from .usuario_schema import GetUsuario
from .termo_schema import GetTermo
from datetime import date


class HistoricoBase(BaseModel):
    usuario: GetUsuario
    termo: GetTermo

    class Config:
        orm_mode = True


class CreateHistorico(BaseModel):
    usuario: int
    termo: int

    class Config:
        orm_mode = True


class GetHistorico(HistoricoBase):
    data: date
