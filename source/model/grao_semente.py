from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class GraoSemente(Base):
    __tablename__ = "gsm_grao_semente"

    id = Column("gsm_id", Integer, primary_key=True, index=True)
    descricao = Column("gsm_descricao", String, index=True)
