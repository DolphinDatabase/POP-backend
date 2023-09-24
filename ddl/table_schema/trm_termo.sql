CREATE TABLE trm_termo (
    trm_id SERIAL PRIMARY KEY,
    trm_data DATE,
    trm_proprietario BOOLEAN,
    trm_text VARCHAR(255)
);