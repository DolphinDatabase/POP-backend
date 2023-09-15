
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from database import Base


class Cultivo(Base):
    __tablename__ = "clt_cultivo"

    id = Column("clt_id", Integer, primary_key=True, index=True)
    descricao = Column("clt_descricao", String, index=True)

    operacao = relationship("Operacao", back_populates="cultivo")
