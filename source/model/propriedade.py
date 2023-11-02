from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Propriedade(Base):
    __tablename__ = "prp_propriedade"

    id = Column("prp_id", Integer, primary_key=True, index=True)
    sncr = Column("prp_sncr", String, index=True)
    nirf = Column("prp_nirf", String, index=True)
    car = Column("prp_car", String, index=True)

    operacao_id = Column("opr_id", Integer, ForeignKey("opr_operacao.opr_id"))
    operacao = relationship("Operacao", back_populates="propriedade")
