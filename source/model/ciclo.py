from sqlalchemy import Column, Integer, String

from database import Base


class Ciclo(Base):
    __tablename__ = "ccl_ciclo"

    id = Column("ccl_id", Integer, primary_key=True, index=True)
    descricao = Column("ccl_descricao", String, index=True)
