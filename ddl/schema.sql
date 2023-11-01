-- Types

CREATE TYPE finalidade_type AS ENUM (
	'Custeio',
	'Comercialização'
);

CREATE TYPE atividade_type AS ENUM (
	'Agrícola'
);

CREATE TYPE modalidade_type AS ENUM (
	'LAVOURA',
	'BENEFICIAMENTO OU INDUSTRIALIZAÇÃO',
	'FEPM (EX-EGF) - encerrado',
	'FEE (EX-LEC)',
	'PRÉ-COMERCIALIZAÇÃO - encerrado',
	'DESCONTO (NPR E DR)',
	'CPR (CÉDULA DE PRODUTO RURAL)',
	'ESTOCAGEM',
	'Aquisição de Matéria Prima direto do Produtor/Coop',
	'FGPP-Financiamento para Garantia de Preços ao Prod',
	'COVID-19 - Resolução 4801/2020',
	'ESTIAGEM - Resolução 4802/2020',
	'Financiamento para Aquisição da Produção/Materia P'
);

CREATE TYPE produto_type AS ENUM (
	'SOJA'
);

CREATE TYPE variedade_type AS ENUM (
	'NÃO SE APLICA',
	'CULTIVO EM SISTEMAS INTEGRADOS',
	'VARIEDADE',
	'SEMENTE',
	'FARELO',
	'ÓLEO BRUTO DEGOMADO',
	'EM GRÃOS',
	'ÓLEO'
);

CREATE TYPE cesta_type AS ENUM (
	'Irrigadas',
	'Safra de Verão (1ª Safra)',
	'Safrinha (2ª Safra)',
	'Ano Civil / Ano de Exploração');

CREATE TYPE zoneamento_type AS ENUM (
	'Não zoneado',
	'Zoneado'
);

-- Tables

CREATE TABLE usr_usuario (
    usr_id SERIAL PRIMARY KEY,
    usr_nome VARCHAR(150),
    usr_doc VARCHAR(14),
    usr_email VARCHAR(255) UNIQUE,
    usr_senha VARCHAR(255),
	usr_grupo VARCHAR(25),
	usr_ativo BOOLEAN
);

CREATE TABLE trm_termo (
    trm_id SERIAL PRIMARY KEY,
    trm_data TIMESTAMP WITHOUT TIME ZONE,
    trm_text TEXT,
	trm_grupo VARCHAR(25)
);

CREATE TABLE trc_termo_condicao (
	trc_id SERIAL PRIMARY KEY,
	trm_id INT,
	trc_texto TEXT,
	trc_servico VARCHAR(255),
	CONSTRAINT fk_trm_id FOREIGN KEY(trm_id) REFERENCES trm_termo(trm_id)
);

CREATE TABLE utr_usuario_termo (
	usr_id INT,
	trm_id INT,
	utr_aceite BOOLEAN,
	utr_data TIMESTAMP WITHOUT TIME ZONE,
	CONSTRAINT fk_usr_id FOREIGN KEY(usr_id) REFERENCES usr_usuario(usr_id),
	CONSTRAINT fk_trm_id FOREIGN KEY(trm_id) REFERENCES trm_termo(trm_id)
);

CREATE TABLE utc_usuario_termo_condicao (
	usr_id INT,
	trc_id INT,
	utc_aceite BOOLEAN,
	utc_data TIMESTAMP WITHOUT TIME ZONE,
	CONSTRAINT fk_usr_id FOREIGN KEY(usr_id) REFERENCES usr_usuario(usr_id),
	CONSTRAINT fk_trc_id FOREIGN KEY(trc_id) REFERENCES trc_termo_condicao(trc_id)
);

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

CREATE TABLE std_estado (
    std_id INT PRIMARY KEY,
    std_descricao VARCHAR(2)
);

CREATE TABLE mun_municipio (
    mun_id BIGINT PRIMARY KEY,
    mun_descricao VARCHAR(255)
);

CREATE TABLE opr_operacao (
    opr_id BIGINT PRIMARY KEY,
    opr_inicio_plantio DATE,
    opr_fim_plantio DATE,
    opr_inicio_colheita DATE,
    opr_fim_colheita DATE,
    std_id INT,
    mun_id BIGINT,
    sol_id INT,
    irg_id INT,
    clt_id INT,
    gsm_id INT,
    ccl_id INT,
    emp_id BIGINT,
	CONSTRAINT fk_std_id FOREIGN KEY(std_id) REFERENCES std_estado(std_id),
	CONSTRAINT fk_mun_id FOREIGN KEY(mun_id) REFERENCES mun_municipio(mun_id),
	CONSTRAINT fk_sol_id FOREIGN KEY(sol_id) REFERENCES sol_solo(sol_id),
	CONSTRAINT fk_irg_id FOREIGN KEY(irg_id) REFERENCES irg_irrigacao(irg_id),
	CONSTRAINT fk_clt_id FOREIGN KEY(clt_id) REFERENCES clt_cultivo(clt_id),
	CONSTRAINT fk_gsm_id FOREIGN KEY(gsm_id) REFERENCES gsm_grao_semente(gsm_id),
	CONSTRAINT fk_ccl_id FOREIGN KEY(ccl_id) REFERENCES ccl_ciclo(ccl_id),
	CONSTRAINT fk_emp_id FOREIGN KEY(emp_id) REFERENCES emp_empreendimento(emp_id)
);

CREATE TABLE glb_gleba (
    glb_id SERIAL PRIMARY KEY,
    glb_poligono geometry(POLYGON,4326),
    opr_id BIGINT,
	CONSTRAINT fk_opr_id FOREIGN KEY(opr_id) REFERENCES opr_operacao(opr_id)
);

CREATE TABLE prp_propriedade (
    prp_id SERIAL PRIMARY KEY,
    prp_doc VARCHAR(14),
    prp_sncr VARCHAR(255),
    prp_nirf VARCHAR(255),
    prp_car VARCHAR(255),
    opr_id BIGINT,
	CONSTRAINT fk_opr_id FOREIGN KEY(opr_id) REFERENCES opr_operacao(opr_id)
);

