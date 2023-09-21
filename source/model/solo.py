from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Solo(Base):
    __tablename__ = "sol_solo"

    id = Column("sol_id", Integer, primary_key=True, index=True)
    descricao = Column("sol_descricao", String, index=True)
