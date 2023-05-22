create table Cliente(
	id int auto_increment not null,
	nome varchar (100) not null,
	cpf varchar (120) not null, 
	cnpj varchar (120), 
	data_nascimento varchar (20),
	endereco varchar (120) not null,
	numero varchar (4),
	cidade varchar(20) not null,
	salario decimal (7, 2) not null,
	desempenho varchar (10) not null, 
	divida varchar (10) not null, 
	risco varchar (20) not null,
	primary key (id)
);
