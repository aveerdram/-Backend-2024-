/*
Напишите SQL запрос для создания и наполнения двух таблиц.
*/

CREATE TABLE Department
(
ID integer primary key,
SALARY varchar(20) not null
);

INSERT INTO supplier VALUES
(1, 'Backend'),
(2, 'DevOps'),
(3, 'Android'),
(4, 'iOS')

CREATE TABLE Users
(
ID integer primary key,
SURNAME varchar(20) not null,
DEPARTMENT_ID integer references supplier (id) on delete set null,
SALARY numeric not null check (price > 0)
);

INSERT INTO supplier VALUES
(1, 'Алексеев', 3, 50000),
(2, 'Петрухин', 3, 60000),
(3, 'Есенин', 2, 70000),
(4, 'Маяковский', 1, 80000),
(5, 'Нортон', 4, 90000),
(6, 'Антропов', 1, 100000),
(7, 'Андреев', 4, 110000),
(8, 'Силантьев', 1, 120000)