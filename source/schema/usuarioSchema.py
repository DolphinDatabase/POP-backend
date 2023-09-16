from pydantic import BaseModel

class UsuarioBase(BaseModel):
    nome:str
    doc:str
    email:str
    class Config:
        orm_mode = True

class CreateUsuario(UsuarioBase):
    proprietario:bool
    senha:str