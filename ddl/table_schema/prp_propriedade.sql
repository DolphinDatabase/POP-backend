CREATE TABLE prp_propriedade (
    prp_id SERIAL PRIMARY KEY,
    prp_sncr VARCHAR(255),
    prp_nirf VARCHAR(255),
    prp_car VARCHAR(255),
    prp_opr BIGINT
);
 
ALTER TABLE prp_propriedade ADD CONSTRAINT FK_prp_opr
    FOREIGN KEY (prp_opr)
    REFERENCES opr_operacao (opr_id);