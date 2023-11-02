from pydantic import BaseModel
from datetime import date


class TermoBase(BaseModel):
    text: str
    proprietario: bool

    class Config:
        orm_mode = True


class GetTermo(TermoBase):
    id: int
    data: date
