CREATE TABLE usr_usuario (
    usr_id SERIAL PRIMARY KEY,
    usr_nome VARCHAR(150),
    usr_email VARCHAR(255),
    usr_senha VARCHAR(255),
    usr_permissao BOOLEAN
)