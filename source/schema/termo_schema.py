from pydantic import BaseModel
from datetime import date
from typing import List


class CondicaoBase(BaseModel):
    param: str


class TermoBase(BaseModel):
    text: str
    grupo: str
    terms: List[CondicaoBase]

    class Config:
        orm_mode = True


class GetTermo(TermoBase):
    id: int
    data: date
