create database personas_db;
create schema personas_db;

use personas_db;

drop schema personas_db;

-- esto es un comentario
-- Create Read Update Delete
create table personas(
	id int primary key auto_increment not null,
    nombre varchar(50) not null,
    apellido varchar(50) not null,
    direccion varchar(100)
    );

-- hacer multiples insets dentro de la tabla personas
insert into personas(nombre, apellido, direccion)
values('Pepito2', 'Morienega2', 'Av san martin'),
	('Pepito3', 'Morienega3', 'Av san juan'),
    ('Pepito4', 'Morienega4', 'Av san lorenzo'),
    ('Pepito5', 'Morienega5', 'Av sarmiento');

-- ver los datos dentro de la tabla persona
select * from personas;
-- ver solamente los nombres y apellido
select nombre, apellido from personas;
--
-- modificar direccion de la tabla personas el id 1
update personas 
set direccion = 'Av Güemes' 
where id=1;

update personas 
set edad = 30
where id=5;

-- eliminar el registro con id 3 
delete from personas where id=3; 

-- modificar la estructura de la tabla(añadimos campo edad)
alter table personas
add column edad int;

-- funciones de sql
select concat(nombre, ' ', apellido) as Personas from personas;
select sum(edad) as 'suma de edades' from personas;
select avg(edad) from personas;
select min(edad) as 'edad minima' from personas;

-- 
select nombre, edad from personas order by edad desc; -- asc
--
select * from personas where edad >= 25;

-- nosotros sabemos que la direccion tiene por sar (_ 1caracter, %no se cantidad de caracteres)
select * from personas where direccion like '___sar%';

-- creando tabala de telefonos(atr multivaludo -> personas)
create table telefonos(
	id int primary key auto_increment not null,
    numero varchar(20) not null,
    tipo varchar(100), -- casa, celular, trabajo
    persona_id int not null,
    foreign key (persona_id) references personas(id)
    );
    
select * from personas;
insert into telefonos(numero, tipo, persona_id)
values('124123423', 'celular', 1),
	('4567454567', 'trabajo', '1'),
    ('456747565', 'casa', '2'),
    ('456776867', 'celular', '4');

-- join + agregando alias (personas que tienen almenos 1 numero de telefono) 
select p.id, p.nombre, p.apellido, t.numero, t.tipo from personas p
join telefonos t on p.id = t.persona_id;

-- inner join
select p.id, p.nombre, p.apellido, t.numero, t.tipo from personas p
inner join telefonos t on p.id = t.persona_id;

-- left join
select p.nombre, p.apellido, ifnull(t.numero, 'sin telefono asociado') as telefonos from personas p left join telefonos t on p.id = t.persona_id;
select p.nombre, p.apellido, t.numero from personas p left join telefonos t on p.id = t.persona_id;

-- subconsultas

-- solo personas con celular
select id, nombre, apellido from personas where id in (select persona_id from telefonos where tipo = 'celular');

-- transacciones

select * from telefonos;

start transaction;
insert into personas(nombre, apellido, direccion)
values ('pedro','sanchez', 'calle Rivadavia');

set @nueva_persona_id = last_insert_id();

insert into telefonos(numero, tipo, persona_id)
values ('456457567','celular', @nueva_persona_id);

-- se vuelve los cambios atras
rollback;
-- confirma los cambios en la bbdd
commit;

