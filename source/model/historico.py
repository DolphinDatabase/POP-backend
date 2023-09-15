from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class Historico(Base):
    __tablename__ = 'htr_historico'

    usuario_id = Column('htr_usr',Integer, ForeignKey('usr_usuario.usr_id'))
    usuario = relationship('User', back_populates="historico")

    termo_id = Column('hrt_trm',Integer, ForeignKey('trm_termo.trm_id'))
    termo = relationship('Term', back_populates="historico")
    
    data = Column('hrt_data',Date)