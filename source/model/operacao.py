from sqlalchemy import Column, ForeignKey, Integer, Date
from sqlalchemy.orm import relationship

from database import Base

class Operacao(Base):
    __tablename__ = "opr_operacao"

    id = Column("opr_id", Integer, primary_key=True, index=True)
    inicio_plantio = Column("opr_inicio_plantio", Date, index=True)
    fim_plantio = Column("opr_fim_plantio", Date, index=True)
    inicio_colheita = Column("opr_inicio_colheita", Date, index=True)
    fim_colheita = Column("opr_fim_colheita", Date, index=True)

    estado_id = Column("opr_estado", Integer, ForeignKey("std_estado.std_id"))
    municipio_id = Column("opr_municipio", Integer, ForeignKey("mun_municipio.mun_id"))


    solo_id = Column("opr_sol", Integer, ForeignKey("sol_solo.sol_id"))
    solo = relationship("Solo", back_populates="operacao")

    irrigacao_id = Column("opr_irg", Integer, ForeignKey("irg_irrigacao.irg_id"))
    irrigacao = relationship("Irrigacao", back_populates="operacao")

    cultivo_id = Column("opr_clt", Integer, ForeignKey("clt_cultivo.clt_id"))
    cultivo = relationship("Cultivo", back_populates="operacao")

    grao_semente_id = Column("opr_gsm", Integer, ForeignKey("gsm_grao_semente.gsm_id"))
    grao_semente = relationship("GraoSemente", back_populates="operacao")

    ciclo_id = Column("opr_ccl", Integer, ForeignKey("ccl_ciclo.ccl_id"))
    ciclo = relationship("Ciclo", back_populates="operacao")

    empreendimento_id = Column("opr_emp", Integer, ForeignKey("emp_empreendimento.emp_id"))
    empreendimento = relationship("Empreendimento", back_populates="operacao")

    gleba = relationship("Gleba", back_populates="operacao")
    propriedade = relationship("Propriedade", back_populates="operacao")
