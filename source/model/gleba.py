from geoalchemy2 import Geography
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from database import Base


class Gleba(Base):
    __tablename__ = "glb_gleba"

    id = Column("glb_id", Integer, primary_key=True, index=True)
    poligono = Column("glb_poligono", Geography('POLYGON'), nullable=False)

    operacao_id = Column("glb_opr", Integer, ForeignKey("opr_operacao.opr_id"))
    operacao = relationship("Operacao", back_populates="gleba")
