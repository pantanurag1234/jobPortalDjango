select * from organisations;
select * from registration;
show tables;

SET SQL_SAFE_UPDATES = 0;

select distinct name,position,experience_in_yrs,package_in_LPA from organisations; 
desc organisations;
delete from organisations;

insert into organisations(name, position, package_in_LPA, experience_in_yrs) values ('Jio','Electronic engineer',6,2);

desc registration;
desc users;
select * from auth_user;
