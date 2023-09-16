from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    senha: str
    # password: str


class User(UserBase):
    id: int
    nome: str
    doc: str
    proprietario: str
    email: str
    senha: str
    permissao: bool
    # is_active: bool

    class Config:
        orm_mode = True


class Propriedade(BaseModel):
    operacao_id: int

    class Config:
        orm_mode = True


class Operacao(BaseModel):
    inicio_plantio: str
    fim_plantio: str
    inicio_colheita: str
    fim_colheita: str
    estado: str
    municipio: str

    solo_id: int
    irrigacao_id: int
    cultivo_id: int
    grao_semente_id: int
    ciclo_id: int
    gleba_id: int
    empreendimento_id: int

    propriedades: list[Propriedade] = []

    class Config:
        orm_mode = True


class Solo(BaseModel):
    class Config:
        orm_mode = True


class Irrigacao(BaseModel):
    class Config:
        orm_mode = True


class Cultivo(BaseModel):
    class Config:
        orm_mode = True


class GraoSemente(BaseModel):
    class Config:
        orm_mode = True


class Ciclo(BaseModel):

    class Config:
        orm_mode = True


class Gleba(BaseModel):
    operacao: Operacao

    class Config:
        orm_mode = True


class Empreendimento(BaseModel):

    operacoes: list[Operacao] = []

    class Config:
        orm_mode = True
