CREATE TABLE opr_operacao (
    opr_id BIGINT PRIMARY KEY,
    opr_inicio_plantio DATE,
    opr_fim_plantio DATE,
    opr_inicio_colheita DATE,
    opr_fim_colheita DATE,
    opr_estado VARCHAR(2),
    opr_municipio VARCHAR(50),
    opr_sol INT,
    opr_irg INT,
    opr_clt INT,
    opr_gsm INT,
    opr_ccl INT,
    opr_emp BIGINT
);
 
ALTER TABLE opr_operacao ADD CONSTRAINT FK_opr_sol
    FOREIGN KEY (opr_sol)
    REFERENCES sol_solo (sol_id);
 
ALTER TABLE opr_operacao ADD CONSTRAINT FK_opr_irg
    FOREIGN KEY (opr_irg)
    REFERENCES irg_irrigacao (irg_id);
 
ALTER TABLE opr_operacao ADD CONSTRAINT FK_opr_clt
    FOREIGN KEY (opr_clt)
    REFERENCES clt_cultivo (clt_id);
 
ALTER TABLE opr_operacao ADD CONSTRAINT FK_opr_gsm
    FOREIGN KEY (opr_gsm)
    REFERENCES gsm_grao_semente (gsm_id);
 
ALTER TABLE opr_operacao ADD CONSTRAINT FK_opr_ccl
    FOREIGN KEY (opr_ccl)
    REFERENCES ccl_ciclo (ccl_id);
 
ALTER TABLE opr_operacao ADD CONSTRAINT FK_opr_emp
    FOREIGN KEY (opr_emp)
    REFERENCES emp_empreendimento (emp_id);