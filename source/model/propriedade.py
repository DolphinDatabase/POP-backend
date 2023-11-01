from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Propriedade(Base):
    __tablename__ = "ppr_propriedade"

    id = Column("ppr_id", Integer, primary_key=True, index=True)
    sncr = Column("ppr_sncr", String, index=True)
    nirf = Column("ppr_nirf", String, index=True)
    car = Column("ppr_car", String, index=True)

    operacao_id = Column("opr_id", Integer, ForeignKey("opr_operacao.opr_id"))
    operacao = relationship("Operacao", back_populates="propriedade")
