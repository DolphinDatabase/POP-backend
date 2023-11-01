from sqlalchemy import Column, Integer, String

from database import Base


class Cultivo(Base):
    __tablename__ = "clt_cultivo"

    id = Column("clt_id", Integer, primary_key=True, index=True)
    descricao = Column("clt_descricao", String, index=True)
