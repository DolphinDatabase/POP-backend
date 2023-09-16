from pydantic import BaseModel
from .usuarioSchema import GetUsuario
from .termoSchema import Termo

class HistoricoBase(BaseModel):
    usuario:GetUsuario
    termo:Termo
    class Config:
        orm_mode = True