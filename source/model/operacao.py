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

    estado_id = Column("std_id", Integer, ForeignKey("std_estado.std_id"))
    estado = relationship("Estado", lazy="selectin")

    municipio_id = Column("mun_id", Integer, ForeignKey("mun_municipio.mun_id"))
    municipio = relationship("Municipio", lazy="selectin")

    solo_id = Column("sol_id", Integer, ForeignKey("sol_solo.sol_id"))
    solo = relationship("Solo", lazy="selectin")

    irrigacao_id = Column("irg_id", Integer, ForeignKey("irg_irrigacao.irg_id"))
    irrigacao = relationship("Irrigacao", lazy="selectin")

    cultivo_id = Column("clt_id", Integer, ForeignKey("clt_cultivo.clt_id"))
    cultivo = relationship("Cultivo", lazy="selectin")

    grao_semente_id = Column("gsm_id", Integer, ForeignKey("gsm_grao_semente.gsm_id"))
    grao_semente = relationship("GraoSemente", lazy="selectin")

    ciclo_id = Column("ccl_id", Integer, ForeignKey("ccl_ciclo.ccl_id"))
    ciclo = relationship("Ciclo", lazy="selectin")

    empreendimento_id = Column("emp_id", Integer, ForeignKey("emp_empreendimento.emp_id"))
    empreendimento = relationship("Empreendimento", lazy="selectin")

    gleba = relationship("Gleba", back_populates="operacao", lazy="selectin")
    propriedade = relationship("Propriedade", back_populates="operacao", lazy="selectin")
