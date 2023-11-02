CREATE TYPE finalidade_type AS ENUM ('Custeio','Comercialização');
CREATE TYPE atividade_type AS ENUM ('Agrícola');
CREATE TYPE modalidade_type AS ENUM ('LAVOURA','BENEFICIAMENTO OU INDUSTRIALIZAÇÃO','FEPM (EX-EGF) - encerrado','FEE (EX-LEC)','PRÉ-COMERCIALIZAÇÃO - encerrado','DESCONTO (NPR E DR)','CPR (CÉDULA DE PRODUTO RURAL)','ESTOCAGEM','Aquisição de Matéria Prima direto do Produtor/Coop','FGPP-Financiamento para Garantia de Preços ao Prod','COVID-19 - Resolução 4801/2020','ESTIAGEM - Resolução 4802/2020','Financiamento para Aquisição da Produção/Materia P');
CREATE TYPE produto_type AS ENUM ('SOJA');
CREATE TYPE variedade_type AS ENUM ('NÃO SE APLICA','CULTIVO EM SISTEMAS INTEGRADOS','VARIEDADE','SEMENTE','FARELO','ÓLEO BRUTO DEGOMADO','EM GRÃOS','ÓLEO');
CREATE TYPE cesta_type AS ENUM ('Irrigadas','Safra de Verão (1ª Safra)','Safrinha (2ª Safra)','Ano Civil / Ano de Exploração');
CREATE TYPE zoneamento_type AS ENUM ('Não zoneado','Zoneado');