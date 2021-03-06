-- seeder.table.standard.standard_manager_db.sql
INSERT INTO standard (
    uuid,
	identification,
	publication_date,
	validity_start,
	title,
	title_global_language,
	comite,
	pages,
	status,
	language,
	organization,
	price,
	currency,
	objective,
	url,
	file,
    deleted,
    created_at
) 
VALUES (
	"067d914c-cb19-4f3f-8755-584e0eafe344",
	"ISO 9000:2015",
	"2015-09-30",
	"2015-10-30",
	"Sistemas de gestão da qualidade - Requisitos",
	"Quality management systems - Fundamentals and vocabulary ",
	"ABNT/CB-025 Qualidade",
	30,
	"Em Vigor",
	"English",
	"ABNT - Associação Brasileira de Normas Técnicas",
	"240.00",
	"BRL",
	"Esta Norma descreve os conceitos fundamentais e princípios de gestão da qualidade que são univer­salmente aplicáveis a: organizações que buscam sucesso sustentado pela implementação de um sistema de gestão da qualidade; clientes que buscam confiança na capacidade de uma organização prover consistentemente produtos e serviços em conformidade com seus requisitos; organizações que buscam confiança de que, em sua cadeia de fornecedores, requisitos de produto e serviço serão atendidos; organizações e partes interessadas que buscam melhorar a comunicação por meio da compre­ensão comum do vocabulário utilizado na gestão da qualidade organizações que fazem avaliação da conformidade com base nos requisitos da ABNT NBR ISO 9001; provedores de treinamento, avaliação ou consultoria em gestão da qualidade; desenvolvedores de normas relacionadas. ",
	"https://www.abntcatalogo.com.br/norma.aspx?ID=345040",
	"https://services.hagatus.com.br/sigo-reader/v1/read/standard/NORMAISO90002015.pdf",
	0,
	"2021-03-14T19:46:00"
),
(
	"36238950-23a3-482a-a73c-2c69498273b4",
	"ISO 9001:2015",
	"2015-09-15",
	"2015-10-30",
	"Quality management systems -- Requirements",
	"Systèmes de management de la qualité-- Exigences",
	"ISO/TC 176 Quality management and quality assurance ",
	29,
	"Em Vigor",
	"English",
	"ISO - International Organization for Standardization",
	"1140.00",
	"BRL",
	"This International Standard specifies requirements for a quality management system when an organization: a) needs to demonstrate its ability to consistently provide products and services that meet customer and applicable statutory and regulatory requirements, and b) aims to enhance customer satisfaction through the effective application of the system, including processes for improvement of the system and the assurance of conformity to customer and applicable statutory and regulatory requirements. ",
	"https://www.abntcatalogo.com.br/norma.aspx?ID=344996",
	"https://services.hagatus.com.br/sigo-reader/v1/read/standard/NORMAISO90012015.pdf",
	0,
	"2021-03-14T19:46:00"
);

