CREATE TABLE glb_gleba (
    glb_id SERIAL PRIMARY KEY,
    glb_poligono geometry(POLYGON,4326),
    glb_opr BIGINT
);

ALTER TABLE glb_gleba ADD CONSTRAINT FK_glb_opr
    FOREIGN KEY (glb_opr)
    REFERENCES opr_operacao (opr_id);