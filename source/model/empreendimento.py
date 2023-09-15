from sqlalchemy import Column, Integer, String

from database import Base


class Empreendimento(Base):
    __tablename__ = "emp_empreendimento"

    id = Column("emp_id", Integer, primary_key=True, index=True)
    finalidade = Column("emp_finalidade", String, index=True)
    atividade = Column("emp_atividade", String, index=True)
    modalidade = Column("emp_modalidade", String, index=True)
    produto = Column("emp_produto", String, index=True)
    variedade = Column("emp_variedade", String, index=True)
    cesta = Column("emp_cesta", String, index=True)
    zoneamento = Column("emp_zoneamento", String, index=True)