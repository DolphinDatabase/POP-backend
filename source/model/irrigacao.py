from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Irrigacao(Base):
    __tablename__ = "irg_irrigacao"

    id = Column("irg_id", Integer, primary_key=True, index=True)
    descricao = Column("irg_descricao", String, index=True)

    operacao = relationship("Operacao", back_populates="irrigacao")

