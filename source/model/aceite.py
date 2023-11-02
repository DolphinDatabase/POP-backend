from sqlalchemy import Column, ForeignKey, Table, Boolean, Integer, DateTime
from sqlalchemy.orm import Mapped, relationship

from database import Base
from .usuario import Usuario


class CondicaoAceite(Base):
    __tablename__ = "utc_usuario_termo_condicao"

    usuario_id = Column(
        "usr_id", Integer, ForeignKey("usr_usuario.usr_id"), primary_key=True
    )
    condicao_id = Column(
        "trc_id", Integer, ForeignKey("trc_termo_condicao.trc_id"), primary_key=True
    )

    aceite = Column("utc_aceite", Boolean)
    data = Column("utc_data", DateTime)

    usuario: Mapped["Usuario"] = relationship()


class TermoAceite(Base):
    __tablename__ = "utr_usuario_termo"

    usuario_id = Column(
        "usr_id", Integer, ForeignKey("usr_usuario.usr_id"), primary_key=True
    )
    termo_id = Column(
        "trm_id", Integer, ForeignKey("trm_termo.trm_id"), primary_key=True
    )

    aceite = Column("utr_aceite", Boolean)
    data = Column("utr_data", DateTime)

    usuario: Mapped["Usuario"] = relationship()
