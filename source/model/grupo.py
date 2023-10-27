from sqlalchemy import Column, Integer, String
from database import Base
from enum import Enum


class GrupoTipo(Enum):
    ADMINISTRADOR = "administrador"
    PROPRIETARIO = "proprietario"
    OPERADOR = "operador"


class Grupo(Base):
    __tablename__ = 'grp_grupo'

    id = Column('grp_id', Integer, primary_key=True, index=True)
    descricao = Column('grp_descricao', String)
