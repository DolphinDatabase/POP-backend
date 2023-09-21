from sqlalchemy import Column, Integer, String, Boolean, Date
from sqlalchemy.orm import relationship
from database import Base


class Termo(Base):
    __tablename__ = 'trm_termo'

    id = Column('trm_id',Integer, primary_key=True, index=True)
    data = Column('trm_data',Date)
    proprietario = Column('trm_proprietario',Boolean)
    text = Column('trm_text',String(255))

    historico = relationship('Historico', back_populates='termo')
