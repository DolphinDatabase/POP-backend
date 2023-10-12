CREATE TABLE usr_usuario (
    usr_id SERIAL PRIMARY KEY,
    usr_nome VARCHAR(150),
    usr_doc VARCHAR(14),
    usr_proprietario BOOLEAN,
    usr_email VARCHAR(255),
    usr_senha VARCHAR(255),
    usr_permissao BOOLEAN
);

CREATE TABLE trm_termo (
    trm_id SERIAL PRIMARY KEY,
    trm_data DATE,
    trm_proprietario BOOLEAN,
    trm_text VARCHAR(255)
);

CREATE TABLE htr_historico (
    htr_usr INT,
    hrt_trm INT,
    hrt_data DATE
);

ALTER TABLE htr_historico ADD CONSTRAINT FK_htr_usr
    FOREIGN KEY (htr_usr)
    REFERENCES usr_usuario(usr_id)
    DELETE ON CASCADE;

ALTER TABLE htr_historico ADD CONSTRAINT FK_htr_trm
    FOREIGN KEY (hrt_trm)
    REFERENCES trm_termo(trm_id);

CREATE TABLE ccl_ciclo (
    ccl_id INT PRIMARY KEY,
    ccl_descricao VARCHAR(150)
);

CREATE TABLE clt_cultivo (
    clt_id INT PRIMARY KEY,
    clt_descricao VARCHAR(150)
);

CREATE TABLE gsm_grao_semente (
    gsm_id INT PRIMARY KEY,
    gsm_descricao VARCHAR(150)
);

CREATE TABLE irg_irrigacao (
    irg_id int PRIMARY KEY,
    irg_descricao VARCHAR(150)
);

CREATE TABLE sol_solo (
    sol_id int PRIMARY KEY,
    sol_descricao VARCHAR(150)
);

CREATE TABLE emp_empreendimento (
    emp_id BIGINT PRIMARY KEY,
    emp_finalidade finalidade_type,
    emp_atividade atividade_type,
    emp_modalidade modalidade_type,
    emp_produto produto_type,
    emp_variedade variedade_type,
    emp_cesta cesta_type,
    emp_zoneamento zoneamento_type
);

CREATE TABLE opr_operacao (
    opr_id BIGINT PRIMARY KEY,
    opr_inicio_plantio DATE,
    opr_fim_plantio DATE,
    opr_inicio_colheita DATE,
    opr_fim_colheita DATE,
    opr_std INT,
    opr_mun BIGINT,
    opr_sol INT,
    opr_irg INT,
    opr_clt INT,
    opr_gsm INT,
    opr_ccl INT,
    opr_emp BIGINT
);

CREATE TABLE std_estado (
    std_id INT PRIMARY KEY,
    std_descricao VARCHAR(2)
);

CREATE TABLE mun_municipio (
    mun_id BIGINT PRIMARY KEY,
    mun_descricao VARCHAR(255)
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

ALTER TABLE opr_operacao ADD CONSTRAINT FK_opr_std
    FOREIGN KEY (opr_std)
    REFERENCES std_estado (std_id);

ALTER TABLE opr_operacao ADD CONSTRAINT FK_opr_mun
    FOREIGN KEY (opr_mun)
    REFERENCES mun_municipio (mun_id);

CREATE TABLE glb_gleba (
    glb_id SERIAL PRIMARY KEY,
    glb_poligono geometry(POLYGON,4326),
    glb_opr BIGINT
);

ALTER TABLE glb_gleba ADD CONSTRAINT FK_glb_opr
    FOREIGN KEY (glb_opr)
    REFERENCES opr_operacao (opr_id);

CREATE TABLE prp_propriedade (
    prp_id SERIAL PRIMARY KEY,
    prp_doc VARCHAR(14),
    prp_sncr VARCHAR(255),
    prp_nirf VARCHAR(255),
    prp_car VARCHAR(255),
    prp_opr BIGINT
);
 
ALTER TABLE prp_propriedade ADD CONSTRAINT FK_prp_opr
    FOREIGN KEY (prp_opr)
    REFERENCES opr_operacao (opr_id);