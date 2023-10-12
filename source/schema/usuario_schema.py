from pydantic import BaseModel


class UsuarioBase(BaseModel):
    nome: str
    doc: str
    email: str

    class Config:
        orm_mode = True


class GetUsuario(UsuarioBase):
    id: int
    proprietario: bool
    adm: bool
    permissao: bool


class CreateUsuario(UsuarioBase):
    proprietario: bool
    adm: bool = False
    senha: str
