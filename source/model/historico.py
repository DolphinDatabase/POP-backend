from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Historico(Base):
    __tablename__ = 'htr_historico'

    usuario_id = Column('htr_usr',Integer, ForeignKey('usr_usuario.usr_id'),primary_key=True)
    usuario = relationship('Usuario', back_populates="historico")

    termo_id = Column('hrt_trm',Integer, ForeignKey('trm_termo.trm_id'),primary_key=True)
    termo = relationship('Termo', back_populates="historico")
    
    data = Column('hrt_data',Date)
