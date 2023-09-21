from pydantic import BaseModel

class UsuarioBase(BaseModel):
    nome:str
    doc:str
    email:str
    class Config:
        orm_mode = True

class GetUsuario(UsuarioBase):
    id:int
    proprietario:bool
    permissao:bool

class CreateUsuario(UsuarioBase):
    proprietario:bool
    senha:str