create database prueba;

use prueba;

create table Usuario(id int, email varchar(255), username varchar(50));

alter table Usuario add edad int;

alter table Usuario drop edad;

alter table Usuario modify column email varchar(50);

insert into Usuario(email, username, edad) values ('ecuador@correo.com', 'aleja', 30);

delete from Usuario where email = 'ecuador@correo.com' limit 3;

alter table Usuario add primary key (id);
alter table Usuario modify column id int auto_increment;

select * from Usuario; 
select * from Usuario where edad <31;

update Usuario set edad = 32 where id = "1";

delete from Usuario where id = "1";