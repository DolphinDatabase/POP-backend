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