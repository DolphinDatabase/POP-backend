from sqlalchemy import Column, Integer, String

from database import Base


class Estado(Base):
    __tablename__ = "std_estado"

    id = Column("std_id", Integer, primary_key=True, index=True)
    descricao = Column("std_descricao", String, index=True)
