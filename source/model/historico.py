from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Historico(Base):
    __tablename__ = 'htr_historico'

    usuario_id = Column('usr_id', Integer, ForeignKey('usr_usuario.usr_id'), primary_key=True)
    usuario = relationship('Usuario', back_populates="historico", lazy='subquery')

    termo_id = Column('trm_id', Integer, ForeignKey('trm_termo.trm_id'), primary_key=True)
    termo = relationship('Termo', back_populates="historico", lazy='subquery')

    data = Column('htr_data', Date)
