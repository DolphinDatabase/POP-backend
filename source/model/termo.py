from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table, Boolean
from sqlalchemy.orm import relationship, Mapped
from database import Base
from typing import List


class Condicao(Base):
    __tablename__ = "trc_termo_condicao"

    id = Column("trc_id", Integer, primary_key=True, index=True)
    texto = Column("trc_texto", String)
    servico = Column("trc_servico", String(255))

    termo_id = Column("trm_id", Integer, ForeignKey("trm_termo.trm_id"))


class Termo(Base):
    __tablename__ = "trm_termo"

    id = Column("trm_id", Integer, primary_key=True, index=True)
    data = Column("trm_data", DateTime)
    texto = Column("trm_text", String)
    grupo = Column("trm_grupo", String)

    condicoes: Mapped[List[Condicao]] = relationship("Condicao", lazy="selectin")
