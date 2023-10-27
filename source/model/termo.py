from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, Mapped
from database import Base
from typing import List


class Termo(Base):
    __tablename__ = 'trm_termo'

    id = Column('trm_id', Integer, primary_key=True, index=True)
    data = Column('trm_data', DateTime)
    texto = Column('trm_text', String)

    grupo_id = Column('grp_id', Integer, ForeignKey('grp_grupo.grp_id'))
    grupo = relationship("Grupo", lazy="selectin")

    condicoes: Mapped[List["Condicao"]] = relationship("Condicao", lazy="selectin")


class Condicao(Base):
    __tablename__ = 'trc_termo_condicao'

    id = Column('trc_id', Integer, primary_key=True, index=True)
    texto = Column('trc_texto', String)

    termo_id = Column('trm_id', Integer, ForeignKey('trm_termo.trm_id'))
    termo = relationship("Termo", lazy="selectin")
