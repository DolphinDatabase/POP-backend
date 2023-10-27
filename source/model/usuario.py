from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
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

    grupo_id = Column("grp_id", Integer, ForeignKey("grp_grupo.grp_id"))
    grupo = relationship("Grupo", lazy="selectin")
