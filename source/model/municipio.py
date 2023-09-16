from sqlalchemy import Column, Integer, String

from database import Base


class Municipio(Base):
    __tablename__ = "mun_municipio"

    id = Column("mun_id", Integer, primary_key=True, index=True)
    descricao = Column("mun_descricao", String, index=True)
