create database magazineluiza;
use magazineluiza;

create table tvs(
	id int auto_increment primary key,
    nome varchar (100),
    preco varchar (90)
);

create table samsung(
	id int auto_increment primary key,
    nome varchar (100),
    preco varchar (90)
);

create table tcl(
	id int auto_increment primary key,
    nome varchar (100),
    preco varchar (90)
);
create table lg(
	id int auto_increment primary key,
    nome varchar (100),
    preco varchar (90)
);
create table multilaser(
	id int auto_increment primary key,
    nome varchar (100),
    preco varchar (90)
);

SET sql_safe_updates = 0;
