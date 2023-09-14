CREATE TABLE htr_historico (
    htr_usr INT,
    hrt_trm INT,
    hrt_data DATE
);

ALTER TABLE htr_historico ADD CONSTRAINT FK_htr_usr
    FOREIGN KEY (htr_usr)
    REFERENCES usr_usuario(usr_id);

ALTER TABLE htr_historico ADD CONSTRAINT FK_htr_trm
    FOREIGN KEY (hrt_trm)
    REFERENCES trm_termo(trm_id);