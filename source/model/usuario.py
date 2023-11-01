from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Usuario(Base):
    __tablename__ = 'usr_usuario'

    id = Column('usr_id', Integer, primary_key=True, index=True)
    nome = Column('usr_nome', String(150))
    doc = Column('usr_doc', String(14))
    email = Column('usr_email', String(255), unique=True)
    senha = Column('usr_senha', String(255))
    grupo = Column("usr_grupo", String(25))
    ativo = Column("usr_ativo", Boolean)
