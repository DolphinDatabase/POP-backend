from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from database import Base


class Usuario(Base):
    __tablename__ = 'usr_usuario'

    id = Column('usr_id', Integer, primary_key=True, index=True)
    nome = Column('usr_nome', String(150))
    doc = Column('usr_doc', String(14))
    proprietario = Column('usr_proprietario', Boolean)
    email = Column('usr_email', String(255))
    senha = Column('usr_senha', String(255))
    permissao = Column('usr_permissao', Boolean)
    adm = Column('usr_adm', Boolean)

    # hashed_password = Column("usr_hashed_password", String)
    # is_active = Column("usr_is_active", Boolean, default=True)

    historico = relationship('Historico', back_populates="usuario")

