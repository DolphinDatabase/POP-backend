COPY public.ccl_ciclo (ccl_id, ccl_descricao) FROM stdin;
1	Grupo I
3	Grupo III
5	Tardio - Desabilitado a partir de dezembro de 2016
6	Desabilitado a partir de dezembro de 2016 - Intermediário
8	Superprecoce - Desabilitado a partir de dezembro de 2016
9	Semiprecoce - Desabilitado a partir de dezembro de 2016
11	Perene
12	Curto - Desabilitado a partir de dezembro de 2016
13	Muito curto - Desabilitado a partir de dezembro de 2016
14	Longo - Desabilitado a partir de dezembro de 2016
15	Semitardio - Desabilitado a partir de dezembro de 2016
16	Grupo V
99	Não informado
4	Grupo IV
2	Grupo II
\.

COPY public.clt_cultivo (clt_id, clt_descricao) FROM stdin;
14	Agroecológica - ENCERRADO
1	Convencional - ENCERRADO
2	Plantio Direto - ENCERRADO
3	Cultivo Mínimo
4	No Toco - ENCERRADO
5	Pré-Germinado
6	Estufa - ENCERRADO
7	Em Galpão - ENCERRADO
8	Hidroponia
9	Extrativismo - ENCERRADO
10	Pecuária Extensiva - ENCERRADO
11	Pecuária Semi-intensiva - ENCERRADO
12	Pecuária Intensiva - ENCERRADO
13	Pecuária Confinamento - ENCERRADO
0	Não se aplica
21	Criação em áreas marinhas delimitadas
22	Criação em ranário
25	cultivo/manejo em floresta pública
16	Criação em Tanques Escavados
18	Criação em Tanques Redes/Fluxo Contínuo
15	CULTIVO PROTEGIDO
20	Substrato
\.

COPY public.emp_empreendimento (emp_id, emp_finalidade, emp_atividade, emp_modalidade, emp_produto, emp_variedade, emp_cesta, emp_zoneamento) FROM stdin;
12016720000052	Custeio	Agrícola	LAVOURA	SOJA	NÃO SE APLICA	Irrigadas	Não zoneado
12016720000013	Custeio	Agrícola	LAVOURA	SOJA	NÃO SE APLICA	Safra de Verão (1ª Safra)	Não zoneado
12016720000023	Custeio	Agrícola	LAVOURA	SOJA	NÃO SE APLICA	Safrinha (2ª Safra)	Não zoneado
12016720000812	Custeio	Agrícola	LAVOURA	SOJA	NÃO SE APLICA	Safra de Verão (1ª Safra)	Não zoneado
12016720000051	Custeio	Agrícola	LAVOURA	SOJA	NÃO SE APLICA	Irrigadas	Zoneado
12016720000022	Custeio	Agrícola	LAVOURA	SOJA	NÃO SE APLICA	Safrinha (2ª Safra)	Não zoneado
12016720000012	Custeio	Agrícola	LAVOURA	SOJA	NÃO SE APLICA	Safra de Verão (1ª Safra)	Não zoneado
12016720000011	Custeio	Agrícola	LAVOURA	SOJA	NÃO SE APLICA	Safra de Verão (1ª Safra)	Zoneado
12016720000053	Custeio	Agrícola	LAVOURA	SOJA	NÃO SE APLICA	Irrigadas	Não zoneado
12016720341011	Custeio	Agrícola	LAVOURA	SOJA	CULTIVO EM SISTEMAS INTEGRADOS	Safra de Verão (1ª Safra)	Zoneado
12036720000002	Custeio	Agrícola	BENEFICIAMENTO OU INDUSTRIALIZAÇÃO	SOJA	NÃO SE APLICA	Ano Civil / Ano de Exploração	Não zoneado
11186720000012	Comercialização	Agrícola	FEPM (EX-EGF) - encerrado	SOJA	NÃO SE APLICA	Safra de Verão (1ª Safra)	Não zoneado
11186720322022	Comercialização	Agrícola	FEPM (EX-EGF) - encerrado	SOJA	VARIEDADE	Safrinha (2ª Safra)	Não zoneado
11206720000408	Comercialização	Agrícola	FEE (EX-LEC)	SOJA	NÃO SE APLICA	Ano Civil / Ano de Exploração	Não zoneado
11206720370408	Comercialização	Agrícola	FEE (EX-LEC)	SOJA	SEMENTE	Ano Civil / Ano de Exploração	Não zoneado
11216720000002	Comercialização	Agrícola	PRÉ-COMERCIALIZAÇÃO - encerrado	SOJA	NÃO SE APLICA	Ano Civil / Ano de Exploração	Não zoneado
11236720000002	Comercialização	Agrícola	DESCONTO (NPR E DR)	SOJA	NÃO SE APLICA	Ano Civil / Ano de Exploração	Não zoneado
11236720156002	Comercialização	Agrícola	DESCONTO (NPR E DR)	SOJA	FARELO	Ano Civil / Ano de Exploração	Não zoneado
11236720219002	Comercialização	Agrícola	DESCONTO (NPR E DR)	SOJA	ÓLEO BRUTO DEGOMADO	Ano Civil / Ano de Exploração	Não zoneado
11236720322011	Comercialização	Agrícola	DESCONTO (NPR E DR)	SOJA	VARIEDADE	Safra de Verão (1ª Safra)	Zoneado
11236720370011	Comercialização	Agrícola	DESCONTO (NPR E DR)	SOJA	SEMENTE	Safra de Verão (1ª Safra)	Zoneado
11246720000002	Comercialização	Agrícola	CPR (CÉDULA DE PRODUTO RURAL)	SOJA	NÃO SE APLICA	Ano Civil / Ano de Exploração	Não zoneado
11256720000002	Comercialização	Agrícola	ESTOCAGEM	SOJA	NÃO SE APLICA	Ano Civil / Ano de Exploração	Não zoneado
11256720156002	Comercialização	Agrícola	ESTOCAGEM	SOJA	FARELO	Ano Civil / Ano de Exploração	Não zoneado
11256720370002	Comercialização	Agrícola	ESTOCAGEM	SOJA	SEMENTE	Ano Civil / Ano de Exploração	Não zoneado
11256720379002	Comercialização	Agrícola	ESTOCAGEM	SOJA	EM GRÃOS	Ano Civil / Ano de Exploração	Não zoneado
11176720000408	Comercialização	Agrícola	Aquisição de Matéria Prima direto do Produtor/Coop	SOJA	NÃO SE APLICA	Ano Civil / Ano de Exploração	Não zoneado
11176720156408	Comercialização	Agrícola	Aquisição de Matéria Prima direto do Produtor/Coop	SOJA	FARELO	Ano Civil / Ano de Exploração	Não zoneado
11176720378408	Comercialização	Agrícola	Aquisição de Matéria Prima direto do Produtor/Coop	SOJA	ÓLEO	Ano Civil / Ano de Exploração	Não zoneado
11306720000011	Comercialização	Agrícola	FGPP-Financiamento para Garantia de Preços ao Prod	SOJA	NÃO SE APLICA	Safra de Verão (1ª Safra)	Zoneado
11306720000012	Comercialização	Agrícola	FGPP-Financiamento para Garantia de Preços ao Prod	SOJA	NÃO SE APLICA	Safra de Verão (1ª Safra)	Não zoneado
11306720000018	Comercialização	Agrícola	FGPP-Financiamento para Garantia de Preços ao Prod	SOJA	NÃO SE APLICA	Safra de Verão (1ª Safra)	Não zoneado
11306720322022	Comercialização	Agrícola	FGPP-Financiamento para Garantia de Preços ao Prod	SOJA	VARIEDADE	Safrinha (2ª Safra)	Não zoneado
12956720000011	Custeio	Agrícola	COVID-19 - Resolução 4801/2020	SOJA	NÃO SE APLICA	Safra de Verão (1ª Safra)	Zoneado
12956720000012	Custeio	Agrícola	COVID-19 - Resolução 4801/2020	SOJA	NÃO SE APLICA	Safra de Verão (1ª Safra)	Não zoneado
12956720000051	Custeio	Agrícola	COVID-19 - Resolução 4801/2020	SOJA	NÃO SE APLICA	Irrigadas	Zoneado
12956720000052	Custeio	Agrícola	COVID-19 - Resolução 4801/2020	SOJA	NÃO SE APLICA	Irrigadas	Não zoneado
12966720000011	Custeio	Agrícola	ESTIAGEM - Resolução 4802/2020	SOJA	NÃO SE APLICA	Safra de Verão (1ª Safra)	Zoneado
12966720000013	Custeio	Agrícola	ESTIAGEM - Resolução 4802/2020	SOJA	NÃO SE APLICA	Safra de Verão (1ª Safra)	Não zoneado
12966720000012	Custeio	Agrícola	ESTIAGEM - Resolução 4802/2020	SOJA	NÃO SE APLICA	Safra de Verão (1ª Safra)	Não zoneado
11336720000408	Comercialização	Agrícola	Financiamento para Aquisição da Produção/Materia P	SOJA	NÃO SE APLICA	Ano Civil / Ano de Exploração	Não zoneado
\.

COPY public.gsm_grao_semente (gsm_id, gsm_descricao) FROM stdin;
0	Não se aplica
3	Semente
8	Grão/Consumo
\.

COPY public.irg_irrigacao (irg_id, irg_descricao) FROM stdin;
1	Não Irrigado
2	Gotejamento
3	Micro-aspersão
4	Aspersão
5	Xique-Xique
6	Pivô
7	Canhão
8	Auto-Propelido
9	Sulcos
10	Inundação
0	Não se aplica
11	Irrigação com cobertura contra a seca MCR 12-2-3-c""
\.

COPY public.mun_municipio (mun_id, mun_descricao) FROM stdin;
4317400	Santiago
4317756	Santo Antônio do Planalto
4318424	São João da Urtiga
4311270	Lagoa dos Três Cantos
4315057	Porto Mauá
4307815	Estrela Velha
4306304	David Canabarro
4307500	Espumoso
4120358	Pranchita
4315503	Restinga Sêca
4316709	Santa Bárbara do Sul
4110052	Iguatu
4119806	Planalto
4321808	Três de Maio
4110607	Iporã
4109807	Ibiporã
4112751	Jesuítas
4304507	Canguçu
4128609	Verê
4309001	Giruá
4104501	Capanema
4322558	Vanini
4309803	Ibiaçá
4316204	Rondinha
4305603	Colorado
4125704	São Miguel do Iguaçu
4311809	Marau
4108205	Formosa do Oeste
4124400	Santo Antônio do Sudoeste
4309951	Ibirapuitã
4323705	Vista Gaúcha
4323457	Vila Nova do Sul
4308458	Fortaleza dos Valos
4304705	Carazinho
4302220	Boa Vista do Cadeado
4116703	Nova Aurora
4310405	Independência
4104808	Cascavel
4123006	Salto do Lontra
4302584	Bozano
4321006	Tapera
4301800	Barracão
4309506	Guarani das Missões
4304309	Cândido Godói
4101002	Ampére
4310439	Ipê
4315354	Quinze de Novembro
4308250	Floriano Peixoto
4321477	Tiradentes do Sul
4301206	Arroio do Tigre
4115309	Mariópolis
4317509	Santo Ângelo
4303707	Campina das Missões
4308854	Gentil
4305871	Coronel Barros
4125209	São Jorge dOeste
4304002	Campo Novo
4304101	Campos Borges
4311155	Jóia
4318606	São José do Ouro
5000856	Angélica
4321402	Tenente Portela
4110706	Irati
4312179	Mato Queimado
4306734	Doutor Maurício Cardoso
4313102	Nova Palma
4310850	Jaboticaba
4100806	Alvorada do Sul
4203501	Campo Erê
4123501	Santa Helena
5003801	Fátima do Sul
4113106	Kaloré
4307401	Esmeralda
4214201	Quilombo
4121257	Ramilândia
4311205	Júlio de Castilhos
4322202	Tupanciretã
4312757	Nova Alvorada
4301958	Barra Funda
4319307	São Paulo das Missões
4314407	Pelotas
4314209	Pedro Osório
4313706	Palmeira das Missões
4318903	São Luiz Gonzaga
4102000	Assis Chateaubriand
4306924	Engenho Velho
4115853	Mercedes
4305306	Chapada
4303202	Cacique Doble
4307450	Esperança do Sul
4103024	Boa Esperança do Iguaçu
4320503	Sertão
4125308	São Jorge do Ivaí
4311254	Lagoão
4320909	Tapejara
3519204	Iacri
4125605	São Mateus do Sul
4322301	Tuparendi
4115457	Marquinho
4104055	Campo Bonito
4106506	Coronel Vivida
4300208	Ajuricaba
4113304	Laranjeiras do Sul
4321907	Três Passos
4311007	Jaguarão
4319604	São Sepé
4307302	Erval Seco
4304655	Capão do Cipó
4115358	Maripá
4317905	Santo Cristo
4320305	Selbach
4306072	Cristal do Sul
4322343	Ubiretama
4302238	Boa Vista do Incra
4121505	Rebouças
4218855	União do Oeste
4127403	Terra Roxa
4118451	Pato Bragado
4323754	Vitória das Missões
4319372	São Pedro do Butiá
4101051	Anahy
4312625	Muliterno
4118808	Peabiru
4315958	Rolador
4304853	Carlos Gomes
4304952	Caseiros
4319158	São Miguel das Missões
4103008	Boa Esperança
4310207	Ijuí
4309704	Humaitá
4320602	Severiano de Almeida
4310504	Iraí
4102752	Bela Vista da Caroba
4313607	Paim Filho
4320404	Serafina Corrêa
4204905	Descanso
4311759	Manoel Viana
4302501	Bossoroca
4305900	Coronel Bicaco
4309159	Gramado Xavier
4323606	Vista Alegre do Prata
4209300	Lages
4311106	Jaguari
4311429	Lajeado do Bugre
4303400	Caiçara
4312658	Não-Me-Toque
4107702	Fênix
4308904	Getúlio Vargas
4320206	Seberi
4128005	Ubiratã
4312955	Nova Boa Vista
4320321	Senador Salgado Filho
4305371	Charrua
4321956	Trindade do Sul
4303301	Caibaté
4109658	Honório Serpa
4112959	Juranda
4314001	Paraí
4311130	Jari
4316600	Sananduva
4123808	Santa Izabel do Oeste
4314068	Passa Sete
4108403	Francisco Beltrão
4112405	Japurá
4313466	Novo Xingu
4111209	Itapejara dOeste
4301503	Augusto Pestana
4305405	Chiapetta
4126355	Serranópolis do Iguaçu
5106240	Nova Ubiratã
4215307	Salete
4128559	Vera Cruz do Oeste
4320578	Sete de Setembro
4211652	Novo Horizonte
4120606	Prudentópolis
4106571	Cruzeiro do Iguaçu
4308656	Garruchos
4123824	Santa Lúcia
4311239	Lagoa Bonita do Sul
4200309	Agronômica
4114609	Marechal Cândido Rondon
4317202	Santa Rosa
4303558	Camargo
4216909	São Lourenço do Oeste
4117271	Nova Tebas
4118105	Paranacity
4105508	Cianorte
4107207	Dois Vizinhos
4103222	Bom Sucesso do Sul
5004007	Glória de Dourados
4316733	Santa Cecília do Sul
4315909	Rodeio Bonito
4310009	Ibirubá
4127858	Três Barras do Paraná
4205605	Galvão
4313805	Palmitinho
5008404	Vicentina
4101705	Araruna
4105409	Chopinzinho
4306130	Cruzaltense
4318804	São Lourenço do Sul
4312351	Montauri
4103453	Cafelândia
4305009	Catuípe
4316436	Saldanha Marinho
4126272	Saudade do Iguaçu
4312906	Nova Bassano
4311601	Liberato Salzano
4319737	São Valério do Sul
4108320	Francisco Alves
4316477	Salvador das Missões
4127205	Terra Boa
4313334	Nova Ramada
5003702	Dourados
4305207	Cerro Largo
4104428	Candói
4321493	Toropi
4318101	São Francisco de Assis
5002704	Campo Grande
4202156	Belmonte
4320800	Soledade
4319109	São Martinho
4313441	Novo Tiradentes
4117909	Palotina
4314100	Passo Fundo
4214607	Rio do Oeste
4124806	São João
4316451	Salto do Jacuí
4322152	Tunas
4320701	Sobradinho
4120655	Quarto Centenário
4116059	Missal
4104451	Cantagalo
4304903	Casca
4321469	Tio Hugo
4314456	Pinhal
4321329	Taquaruçu do Sul
4115739	Mato Rico
4315107	Porto Xavier
4101101	Andirá
4113403	Leópolis
4300471	Almirante Tamandaré do Sul
4108809	Guaíra
4212700	Petrolândia
4115804	Medianeira
4322707	Vera Cruz
4320651	Silveira Martins
4107538	Entre Rios do Oeste
4219150	Vargem
4315008	Porto Lucena
4315701	Rio Pardo
4110805	Iretama
4107405	Enéas Marques
4314134	Paulo Bento
4318309	São Gabriel
4312203	Maximiliano de Almeida
4127700	Toledo
4312138	Mato Castelhano
5005251	Laguna Carapã
4312708	Nonoai
5000609	Amambai
4316105	Ronda Alta
4306767	Eldorado do Sul
4105003	Catanduvas
4312427	Mormaço
4107157	Diamante DOeste
4312302	Miraguaí
4114807	Marialva
4211009	Mondaí
4306007	Crissiumal
4311908	Marcelino Ramos
4122156	Rio Bonito do Iguaçu
4301909	Barra do Ribeiro
4207403	Imbuia
4117222	Nova Santa Rosa
4310413	Inhacorá
4301925	Barra do Rio Azul
4323358	Vila Lângaro
4316428	Sagrada Família
4314704	Planalto
4116901	Nova Esperança
4313904	Panambi
4304622	Capão Bonito do Sul
4108601	Goioerê
4104303	Campo Mourão
4300505	Alpestre
4309654	Hulha Negra
4323408	Vila Maria
4119004	Pérola dOeste
4322350	União da Serra
4316303	Roque Gonzales
4305157	Cerro Grande
4310876	Jacuizinho
4313425	Novo Machado
4300455	Alegria
4107553	Farol
4306320	Derrubadas
4321857	Três Palmeiras
4214151	Princesa
4201901	Aurora
4318002	São Borja
4119251	Pinhal de São Bento
4101150	Ângulo
4306932	Entre-Ijuís
4203402	Campo Belo do Sul
3541604	Promissão
5006606	Ponta Porã
4115606	Matelândia
4302600	Braga
4311502	Lavras do Sul
4305975	Coxilha
4117404	Ourizona
4309407	Guaporé
4316907	Santa Maria
4300109	Agudo
4305801	Constantina
4309902	Ibiraiaras
4314027	Paraíso do Sul
4321634	Três Arroios
4313490	Novo Barreiro
4317806	Santo Augusto
4117453	Ouro Verde do Oeste
4323101	Vicente Dutra
4126405	Sertaneja
4306106	Cruz Alta
4313300	Nova Prata
4104600	Capitão Leônidas Marques
4305504	Ciríaco
4301404	Arvorezinha
4111407	Ivaí
4303509	Camaquã
4316972	Santa Margarida do Sul
4204202	Chapecó
4314308	Pejuçara
4107306	Doutor Camargo
4314472	Pinhal Grande
4216800	São José do Cerrito
4201273	Arabutã
3530201	Mirante do Paranapanema
4322103	Tucunduva
4308300	Fontoura Xavier
4320263	Segredo
4120903	Quedas do Iguaçu
5002407	Caarapó
4105706	Clevelândia
4323200	Victor Graeff
4313011	Nova Candelária
4206801	Ibicaré
4206207	Gravatal
4217550	Serra Alta
4123204	Santa Cecília do Pavão
4113429	Lidianópolis
4307005	Erechim
4307831	Eugênio de Castro
4322186	Tupanci do Sul
4317954	Santo Expedito do Sul
4301701	Barão de Cotegipe
5004106	Guia Lopes da Laguna
4116950	Nova Esperança do Sudoeste
4204194	Chapadão do Lageado
4303004	Cachoeira do Sul
4118501	Pato Branco
4322533	Vale do Sol
4322608	Venâncio Aires
4313037	Nova Esperança do Sul
4204178	Cerro Negro
4103040	Boa Ventura de São Roque
4319406	São Pedro do Sul
4300554	Alto Alegre
4206405	Guaraciaba
4113007	Jussara
4315313	Quatro Irmãos
4110656	Iracema do Oeste
4305124	Cerrito
4101853	Ariranha do Ivaí
4127908	Tuneiras do Oeste
4102505	Barbosa Ferraz
4315172	Protásio Alves
4105300	Céu Azul
4112207	Janiópolis
4111506	Ivaiporã
4107801	Floraí
4310751	Ivorá
4125001	São João do Ivaí
4310462	Ipiranga do Sul
4117255	Nova Prata do Iguaçu
4301305	Arroio Grande
4305116	Centenário
4314605	Piratini
4107546	Espigão Alto do Iguaçu
4317558	Santo Antônio do Palma
4318465	São José do Herval
3137502	Lagoa Formosa
4201802	Atalanta
4319208	São Nicolau
4300703	Anta Gorda
4307864	Fagundes Varela
4110953	Itaipulândia
4117057	Nova Laranjeiras
4210902	Modelo
4302006	Barros Cassal
4300406	Alegrete
4123857	Santa Maria do Oeste
4202875	Brunópolis
1701903	Araguacema
4314787	Ponte Preta
4104402	Cândido de Abreu
4302055	Benjamin Constant do Sul
4308508	Frederico Westphalen
4204806	Curitibanos
4320107	Sarandi
4310579	Itapuca
4314464	Pinhal da Serra
4315073	Porto Vera Cruz
4119608	Pitanga
4319802	São Vicente do Sul
4302204	Boa Vista do Buricá
4106407	Cornélio Procópio
4311700	Machadinho
4309126	Gramado dos Loureiros
4113734	Luiziana
4208500	Ituporanga
4203600	Campos Novos
4315453	Relvado
4121406	Realeza
4304200	Candelária
4315800	Roca Sales
4114401	Mangueirinha
4107504	Engenheiro Beltrão
4310553	Itacurubi
5007406	Rio Verde de Mato Grosso
4311304	Lagoa Vermelha
5007695	São Gabriel do Oeste
4116109	Moreira Sales
5005681	Mundo Novo
4318457	São José das Missões
4219408	Witmarsum
4300901	Aratiba
4113205	Lapa
4205209	Erval Velho
4322905	Viadutos
4315404	Redentora
4102604	Barracão
4219200	Vidal Ramos
4106308	Corbélia
4304663	Capão do Leão
4111100	Itambé
4125753	São Pedro do Iguaçu
4313953	Pantano Grande
4311718	Maçambará
4113908	Mallet
4301552	Áurea
5216452	Perolândia
4314555	Pirapó
4306205	Cruzeiro do Sul
4307054	Ernestina
4204400	Coronel Freitas
4320354	Sentinela do Sul
4319703	São Valentim
4300307	Alecrim
4126652	Sulina
4211058	Monte Carlo
4312104	Mata
4109302	Guaraniaçu
4302154	Boa Vista das Missões
4309753	Ibarama
4312674	Nicolau Vergueiro
4128708	Vitorino
4123709	Santa Isabel do Ivaí
3137536	Lagoa Grande
4315321	Quevedos
4117800	Palmital
4315552	Rio dos Índios
4308003	Faxinal do Soturno
4207684	Ipuaçu
4316402	Rosário do Sul
4120507	Primeiro de Maio
4106852	Cruzmaltina
4219358	Vitor Meireles
4113452	Lindoeste
4102109	Astorga
4116802	Nova Cantu
4317707	Santo Antônio das Missões
4118006	Paraíso do Norte
4120150	Porto Barreiro
4121604	Renascença
4120853	Quatro Pontes
4108304	Foz do Iguaçu
4108007	Florestópolis
4309258	Guabiju
1100320	São Miguel do Guaporé
4101655	Arapuã
4124053	Santa Terezinha de Itaipu
4103057	Boa Vista da Aparecida
4126108	São Tomé
4108106	Flórida
4100707	Alto Piquiri
4114500	Manoel Ribas
4121109	Quinta do Sol
4205001	Dionísio Cerqueira
4313391	Novo Cabrais
4204301	Concórdia
4206603	Guarujá do Sul
4316808	Santa Cruz do Sul
4218608	Trombudo Central
4115200	Maringá
4216701	São José do Cedro
4208104	Itaiópolis
4305702	Condor
5006200	Nova Andradina
4318499	São José do Inhacorá
4121356	Rancho Alegre DOeste
4300059	Água Santa
4100509	Altônia
4313359	Nova Roma do Sul
4306056	Cristal
4106001	Congonhinhas
4200051	Abdon Batista
4306957	Entre Rios do Sul
4305835	Coqueiro Baixo
5004601	Itaquiraí
4302907	Cacequi
4200408	Água Doce
4108551	Godoy Moreira
3502804	Araçatuba
4125357	São Jorge do Patrocínio
4208401	Itapiranga
4103156	Bom Jesus do Sul
4200200	Agrolândia
5005152	Juti
4308052	Faxinalzinho
4127957	Tupãssi
4203907	Capinzal
4314779	Pontão
4125803	São Pedro do Ivaí
4303673	Campestre da Serra
4310702	Itatiba do Sul
3535804	Paranapanema
4117701	Palmeira
5000807	Anaurilândia
3115805	Centralina
4214508	Rio do Campo
4323309	Vila Flores
5003454	Deodápolis
4217907	Tangará
4209177	Jupiá
4125555	São Manoel do Paraná
4202602	Bom Retiro
4319711	São Valentim do Sul
4106555	Corumbataí do Sul
4103370	Brasilândia do Sul
4205431	Formosa do Sul
4213708	Pouso Redondo
4125100	São João do Triunfo
4319364	São Pedro das Missões
4306908	Encruzilhada do Sul
4312450	Morro Redondo
4103305	Borrazópolis
4207908	Irineópolis
4215554	Santa Helena
4301859	Barra do Guarita
5001243	Aral Moreira
4310538	Itaara
4103909	Campina da Lagoa
4124608	São Carlos do Ivaí
4303806	Campinas do Sul
4309605	Horizontina
4304358	Candiota
4103958	Campina do Simão
4108957	Guamiranga
4203808	Canoinhas
4204459	Coronel Martins
4103479	Cafezal do Sul
3528809	Maracaí
4210308	Major Vieira
4306353	Dezesseis de Novembro
4110102	Imbituva
4215679	Santa Terezinha
4215695	Santiago do Sul
4305132	Cerro Branco
4200754	Alto Bela Vista
4121703	Reserva
4202081	Bandeirante
4306601	Dom Pedrito
4323002	Viamão
5007208	Rio Brilhante
4205555	Frei Rogério
4123402	Santa Fé
5100201	Água Boa
4101903	Assaí
4300661	André da Rocha
4318051	São Domingos do Sul
5003504	Douradina
4124202	Santo Antônio do Caiuá
5205471	Chapadão do Céu
4114005	Mamborê
4215208	Romelândia
4314498	Pinheirinho do Vale
4307559	Estação
4307104	Herval
4310603	Itaqui
4118600	Paula Freitas
4319125	São Martinho da Serra
4124020	Santa Tereza do Oeste
4112108	Jandaia do Sul
4216107	São Domingos
4217204	São Miguel do Oeste
4306759	Doutor Ricardo
4106605	Cruzeiro do Oeste
4306379	Dilermando de Aguiar
4207858	Irati
4106803	Cruz Machado
4306973	Erebango
4322525	Vale Verde
5204409	Caiapônia
4107850	Flor da Serra do Sul
4320230	Sede Nova
4308409	Formigueiro
4122107	Rio Bom
4211751	Otacílio Costa
4205506	Fraiburgo
4104907	Castro
4207650	Iporã do Oeste
4112504	Jardim Alegre
3507753	Brejo Alegre
4103206	Bom Sucesso
5001508	Bandeirantes
4322806	Veranópolis
4208609	Jaborá
4115408	Marmeleiro
4122008	Rio Azul
4317004	Santana da Boa Vista
4217303	Saudades
4200507	Águas de Chapecó
4302378	Bom Progresso
4103404	Cafeara
4310900	Jacutinga
4322400	Uruguaiana
5006259	Novo Horizonte do Sul
4317103	SantAna do Livramento
4310306	Ilópolis
4122503	Roncador
4124707	São Jerônimo da Serra
4200804	Anchieta
4102208	Atalaia
4312807	Nova Araçá
4307807	Estrela
4103602	Cambará
4203105	Caibi
4109401	Guarapuava
4201000	Anita Garibaldi
4209508	Laurentino
5003488	Dois Irmãos do Buriti
4312500	Mostardas
3533700	Ocauçu
4219705	Xaxim
4118709	Paulo Frontin
3506508	Birigui
4128658	Virmond
4103354	Braganey
4108452	Foz do Jordão
4308706	Gaurama
4211454	Nova Itaberaba
5004809	Japorã
4322509	Vacaria
4127965	Turvo
4323507	Vista Alegre
5003751	Eldorado
4305959	Cotiporã
4102901	Bituruna
4209904	Lontras
4203006	Caçador
4206702	Herval dOeste
4128807	Xambrê
4121000	Querência do Norte
4204152	Celso Ramos
4213104	Piratuba
4302709	Butiá
4312617	Muitos Capões
4207759	Iraceminha
4122800	Salgado Filho
5219308	Santa Helena de Goiás
4126009	São Sebastião da Amoreira
4217501	Seara
4212239	Paraíso
5219357	Santa Isabel
4318440	São Jorge
4213351	Ponte Alta do Norte
4108650	Goioxim
4109104	Guaporema
4301602	Bagé
4321105	Tapes
4314506	Pinheiro Machado
4306502	Dom Feliciano
4127502	Tibagi
3535507	Paraguaçu Paulista
4100459	Altamira do Paraná
4107108	Diamante do Norte
4315206	Putinga
4314175	Pedras Altas
5004502	Itaporã
4119301	Pinhão
4107256	Douradina
4321451	Teutônia
5210901	Itapaci
4128500	Wenceslau Braz
4116307	Munhoz de Melo
5007703	Sete Quedas
4124103	Santo Antônio da Platina
4122602	Rondon
3506300	Bernardino de Campos
4218301	Três Barras
4302303	Bom Jesus
4128302	Uniflor
4109757	Ibema
4305850	Coqueiros do Sul
4124509	Santo Inácio
4320677	Sinimbu
4318408	São Jerônimo
4301750	Barão do Triunfo
4312005	Mariano Moro
4300638	Amaral Ferrador
4305587	Colinas
4307203	Erval Grande
4312252	Minas do Leão
4212106	Palmitos
4302808	Caçapava do Sul
4107603	Faxinal
4300646	Ametista do Sul
4301107	Arroio dos Ratos
4320552	Sertão Santana
4317301	Santa Vitória do Palmar
4306452	Dois Lajeados
4105102	Centenário do Sul
4306429	Dois Irmãos das Missões
4315305	Quaraí
4306700	Dona Francisca
4122701	Sabáudia
4322327	Turuçu
4206751	Ibiam
3526704	Leme
5007950	Tacuru
4214805	Rio do Sul
4110508	Ipiranga
4207007	Içara
4107900	Floresta
4118857	Perobal
1718758	Rio Sono
4302451	Boqueirão do Leão
5007901	Sidrolândia
3503406	Arealva
4306809	Encantado
5221551	Turvelândia
4109906	Icaraíma
3535002	Palestina
2105476	Jenipapo dos Vieiras
4314076	Passo do Sobrado
4112702	Jataizinho
5207352	Edealina
4308805	General Câmara
4114104	Mandaguaçu
4200556	Águas Frias
4111001	Itambaracá
4215000	Rio Negrinho
4125456	São José das Palmeiras
3553955	Tarumã
4315156	Progresso
4210100	Mafra
4115101	Mariluz
4128104	Umuarama
4301073	Arroio do Padre
4127007	Teixeira Soares
4107009	Curiúva
5200134	Acreúna
4312153	Mato Leitão
4300851	Arambaré
4122172	Rio Branco do Ivaí
4101804	Araucária
4210555	Marema
4117503	Paiçandu
4315602	Rio Grande
4309050	Glorinha
4214102	Presidente Nereu
5216403	Paraúna
4113759	Lunardelli
4102307	Balsa Nova
4309571	Herveiras
4117008	Nova Fátima
5212105	Joviânia
4206652	Guatambú
4108908	Guairaçá
2107902	Passagem Franca
4204350	Cordilheira Alta
4128401	Uraí
4210852	Mirim Doce
4311981	Mariana Pimentel
4204004	Catanduvas
3525607	João Ramalho
4322855	Vespasiano Corrêa
5004304	Iguatemi
4207809	Irani
3519907	Iepê
4200705	Alfredo Wagner
4313409	Novo Hamburgo
4119509	Piraquara
3169307	Três Corações
4110409	Indianópolis
3537156	Pedrinhas Paulista
4123907	Santa Mariana
4126504	Sertanópolis
5209937	Inaciolândia
4110300	Inajá
3530805	Mogi Mirim
4208955	Jardinópolis
3546405	Santa Cruz do Rio Pardo
5002001	Batayporã
4107736	Fernandes Pinheiro
5005103	Jateí
4203253	Capão Alto
4301008	Arroio do Meio
4204707	Cunha Porã
4211405	Nova Erechim
4316758	Santa Clara do Sul
5005400	Maracaju
4123105	Santa Amélia
4321626	Travesseiro
5007976	Taquarussu
4305355	Charqueadas
4115903	Mirador
3162005	São Gonçalo do Sapucaí
5007554	Santa Rita do Pardo
5103858	Gaúcha do Norte
3513306	Cruzália
4313656	Palmares do Sul
4211801	Ouro
4219309	Videira
5211503	Itumbiara
5008008	Terenos
4111902	Jaguapitã
4217808	Taió
4126702	Tamboara
4126256	Sarandi
4113700	Londrina
4219176	Vargem Bonita
5218508	Quirinópolis
4114351	Manfrinópolis
5005806	Nioaque
2110658	São Domingos do Azeitão
4312377	Monte Alegre dos Campos
4318432	São João do Polêsine
5106307	Paranatinga
4115507	Marumbi
4211850	Ouro Verde
4120408	Presidente Castelo Branco
3542909	Ribeirão Bonito
4202099	Barra Bonita
4104105	Campo do Tenente
4108700	Grandes Rios
4300802	Antônio Prado
4110003	Iguaraçu
3514700	Echaporã
4202438	Bocaina do Sul
4100905	Amaporã
4212007	Palma Sola
4210506	Maravilha
4108502	General Carneiro
5213004	Maurilândia
4215752	São Bernardino
4119400	Piraí do Sul
4209458	Lajeado Grande
3542206	Rancharia
4123956	Santa Mônica
5004700	Ivinhema
4214003	Presidente Getúlio
5005707	Naviraí
2106607	Matões
4215687	Santa Terezinha do Progresso
4201653	Arvoredo
4121208	Quitandinha
4119905	Ponta Grossa
4126603	Siqueira Campos
4322376	Unistalda
4117214	Nova Santa Bárbara
4126801	Tapejara
4214409	Rio das Antas
5221700	Uruana
3544251	Rosana
4317608	Santo Antônio da Patrulha
4111704	Jaboti
3509809	Campos Novos Paulista
4104253	Campo Magro
1703701	Brejinho de Nazaré
4121752	Reserva do Iguaçu
3531407	Monte Aprazível
5210109	Ipameri
5002209	Bonito
4321204	Taquara
4311403	Lajeado
3503208	Araraquara
4106209	Contenda
4202859	Braço do Trombudo
4204103	Caxambu do Sul
4219507	Xanxerê
4212908	Pinhalzinho
4219853	Zortéa
4213609	Porto União
3537503	Pereiras
4109708	Ibaiti
4122651	Rosário do Ivaí
4207601	Ipira
4110201	Inácio Martins
3512704	Corumbataí
4101408	Apucarana
4209201	Lacerdópolis
3553856	Taquarivaí
5204508	Caldas Novas
4312609	Muçum
4212205	Papanduva
5107180	Ribeirão Cascalheira
4111555	Ivaté
4100608	Alto Paraná
2101400	Balsas
1717503	Pium
5003157	Coronel Sapucaia
4300034	Aceguá
4113809	Lupionópolis
4213302	Ponte Alta
4124301	Santo Antônio do Paraíso
3533908	Olímpia
4121307	Rancho Alegre
4128534	Ventania
5002100	Bela Vista
3540903	Pradópolis
3510807	Casa Branca
3144102	Muzambinho
3515301	Estrela do Norte
3534708	Ourinhos
3525706	José Bonifácio
4215356	Saltinho
4118402	Paranavaí
4314803	Portão
5205059	Castelândia
3141900	Minduri
4116604	Nova América da Colina
5201306	Anicuns
4323770	Westfália
1702000	Araguaçu
3153400	Presidente Olegário
4125407	São José da Boa Vista
4305439	Chuí
2111607	São Raimundo das Mangabeiras
1715259	Novo Jardim
4119707	Planaltina do Paraná
5215900	Palminópolis
3545407	Salto Grande
4202578	Bom Jesus do Oeste
4216008	São Carlos
5216007	Panamá
5220603	Silvânia
3539301	Pirassununga
4309209	Gravataí
1706258	Crixás do Tocantins
4217956	Tigrinhos
4205100	Dona Emma
3103801	Arapuá
4201604	Arroio Trinta
4123303	Santa Cruz de Monte Castelo
3517109	Glicério
4322004	Triunfo
3120201	Cristais
5204250	Cachoeira Dourada
3535309	Palmital
4124004	Santana do Itararé
4114203	Mandaguari
3143203	Monte Santo de Minas
4113601	Lobato
3530508	Mococa
4112900	Jundiaí do Sul
3534757	Ouroeste
5204805	Campo Alegre de Goiás
1100205	Porto Velho
3522802	Itaporanga
3552908	Taciba
5004908	Jaraguari
4207700	Ipumirim
2909307	Correntina
4111605	Ivatuba
5204003	Cabeceiras
5102702	Canarana
4102406	Bandeirantes
5218805	Rio Verde
5006002	Nova Alvorada do Sul
4312054	Marques de Souza
3551900	Severínia
5209101	Goiatuba
4212601	Peritiba
4215075	Riqueza
4128625	Alto Paraíso
4209706	Lebon Régis
3522703	Itápolis
4107124	Diamante do Sul
4103503	Califórnia
3509452	Campina do Monte Alegre
4106704	Cruzeiro do Sul
5006358	Paranhos
1710508	Itacajá
5103700	Feliz Natal
3518206	Guararapes
5210158	Ipiranga de Goiás
3544400	Rubiácea
3504008	Assis
4101507	Arapongas
4304606	Canoas
4122305	Rio Negro
4213153	Planalto Alegre
4100103	Abatiá
4305173	Cerro Grande do Sul
5215306	Orizona
1721257	Tupirama
2928901	São Desidério
5003256	Costa Rica
5001904	Bataguassu
3543204	Ribeirão do Sul
4102802	Bela Vista do Paraíso
5007505	Rochedo
3111804	Canápolis
4314159	Paverama
4217758	Sul Brasil
3126208	Formoso
5210802	Itajá
4121901	Ribeirão do Pinhal
4202131	Bela Vista do Toldo
4203303	Campo Alegre
4118303	Paranapoema
3170107	Uberaba
3134202	Ituiutaba
4209151	José Boiteux
4209805	Leoberto Leal
4217154	São Miguel da Boa Vista
4127809	Tomazina
3517406	Guaíra
4117602	Palmas
4101606	Arapoti
3550506	São Pedro do Turvo
2211209	Uruçuí
3169604	Tupaciguara
3162948	São José da Barra
4315131	Pouso Novo
4308078	Fazenda Vilanova
5207808	Firminópolis
3554201	Tejupá
3142809	Monte Alegre de Minas
4211108	Monte Castelo
3519501	Ibirarema
4111803	Jacarezinho
5217708	Pontalina
1500602	Altamira
5215603	Padre Bernardo
3510302	Capela do Alto
4110904	Itaguajé
5001102	Aquidauana
5212501	Luziânia
4110078	Imbaú
2917359	Jaborandi
4216057	São Cristóvão do Sul
5106505	Poconé
4118907	Pérola
4117297	Novo Itacolomi
4311122	Jaquirana
3127107	Frutal
4313060	Nova Hartz
1400175	Cantá
1700350	Aliança do Tocantins
4203154	Calmon
3511508	Cerquilho
3540804	Potirendaba
4116406	Nossa Senhora das Graças
4304408	Canela
3537305	Penápolis
3522406	Itapeva
4104204	Campo Largo
3148004	Patos de Minas
5222005	Vianópolis
4204558	Correia Pinto
3532603	Nhandeara
4113254	Laranjal
4101309	Antônio Olinto
3163904	São Pedro da União
3147204	Paraguaçu
3536703	Pederneiras
4314050	Parobé
4304713	Caraá
3524501	Jaci
4209003	Joaçaba
4215505	Santa Cecília
3136900	Juruaia
5218607	Rialma
4204608	Criciúma
5205109	Catalão
4204756	Cunhataí
4202537	Bom Jesus
4128203	União da Vitória
4212270	Passos Maia
3506003	Bauru
5219209	Santa Cruz de Goiás
3505203	Bariri
3140506	Martinho Campos
4103800	Cambira
3512506	Coroados
4309308	Guaíba
5002803	Caracol
3510005	Cândido Mota
5219100	Santa Bárbara de Goiás
3102001	Alterosa
3522307	Itapetininga
3147006	Paracatu
4321352	Tavares
5222054	Vicentinópolis
4126207	Sapopema
3532504	Neves Paulista
4102703	Barra do Jacaré
3554300	Teodoro Sampaio
4106456	Coronel Domingos Soares
4212056	Palmeira
3537909	Pilar do Sul
5219456	Santa Rita do Novo Destino
3526902	Limeira
3504503	Avaré
4117305	Ortigueira
4218707	Tubarão
3527108	Lins
4321303	Taquari
4216255	São João do Oeste
4104709	Carlópolis
4114906	Marilândia do Sul
4117206	Nova Olímpia
4308201	Flores da Cunha
4218756	Tunápolis
3540705	Porto Ferreira
5002308	Brasilândia
2201309	Barreiras do Piauí
3157708	Santa Juliana
3545506	Sandovalina
4208005	Itá
4120333	Prado Ferreira
4304697	Capitão
4218251	Timbó Grande
3543238	Ribeirão dos Índios
4205175	Entre Rios
4305447	Chuvisca
4205308	Faxinal dos Guedes
4127601	Tijucas do Sul
3508108	Buritama
1502939	Dom Eliseu
3164407	São Sebastião da Bela Vista
4219606	Xavantina
5000708	Anastácio
5106174	Nova Nazaré
4126306	Sengés
1400050	Alto Alegre
3101607	Alfenas
4124905	São João do Caiuá
5200506	Aloândia
3146008	Ouro Fino
1502301	Capitão Poço
3545803	Santa Bárbara dOeste
4200101	Abelardo Luz
3538709	Piracicaba
4218509	Treze Tílias
4111308	Itaúna do Sul
5213806	Morrinhos
4215406	Salto Veloso
4209854	Lindóia do Sul
\.

COPY public.sol_solo (sol_id, sol_descricao) FROM stdin;
1	Solo arenoso
2	Solo com textura média
3	Solo argiloso
9	Tipo de solo desconhecido
\.

COPY public.std_estado (std_id, std_descricao) FROM stdin;
10	BA
8	GO
6	MA
9	MG
3	MS
5	MT
11	PA
12	PI
1	PR
14	RO
13	RR
0	RS
2	SC
4	SP
7	TO
\.

COPY public.opr_operacao (opr_id, opr_inicio_plantio, opr_fim_plantio, opr_inicio_colheita, opr_fim_colheita, std_id, mun_id, sol_id, irg_id, clt_id, gsm_id, ccl_id, emp_id) FROM stdin;
5087149171	2019-11-20	2019-11-30	2020-03-17	2020-03-18	0	4307500	3	1	2	8	2	12016720000011
5126285181	2021-10-06	2021-10-06	2022-01-30	2022-02-15	1	4102000	3	1	0	8	1	12016720000011
\.

COPY public.glb_gleba (glb_id, glb_poligono, opr_id) FROM stdin;
8	0103000020E610000001000000140000004777103B53A44AC068CBB914571D3BC0B1169F0260A44AC0E96514CB2D1D3BC01CD3139678A44AC04CC3F011311D3BC0CD1E680586A44AC0F6234564581D3BC00DC347C494A44AC0CC6262F3711D3BC0BF2B82FFADA44AC012A0A696AD1D3BC0A2B437F8C2A44AC004CAA65CE11D3BC0F7E461A1D6A44AC0AE64C746201E3BC031D3F6AFACA44AC0AEF545425B1E3BC0EAB298D87CA44AC066DAFE95951E3BC06A6AD95A5FA44AC0BB270F0BB51E3BC0CE70033E3FA44AC09F5912A0A61E3BC0C0CFB87020A44AC0037D224F921E3BC0B98D06F016A44AC011363CBD521E3BC0551344DD07A44AC075E5B33C0F1E3BC024B9FC87F4A34AC0A089B0E1E91D3BC080B74082E2A34AC0F6622827DA1D3BC0AB9509BFD4A34AC0A06CCA15DE1D3BC0C078060DFDA34AC0842A357BA01D3BC04777103B53A44AC068CBB914571D3BC0	5126285181
12	0103000020E610000001000000050000007E198C1189524EC06806F1811D7F0040BA66F2CD36534EC0B2BCAB1E306F004008E9297288524EC06440F67AF7670040054F2157EA514EC012F92EA52E7900407E198C1189524EC06806F1811D7F0040	5087149171
\.
