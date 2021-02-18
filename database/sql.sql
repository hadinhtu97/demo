--  select 
SELECT *
FROM table_name;

SELECT column_1, column_2
FROM table_name;

-- distinct
SELECT DISTINCT *
FROM table_name;

-- where
SELECT *
FROM table_name
WHERE condition;

SELECT *
FROM table_name
WHERE condition AND condition;

SELECT *
FROM table_name
WHERE condition OR condition;

-- order by
SELECT *
FROM table_name
ORDER BY column;

select *
from table_name
ORDER by column1, column2 DESC;

-- top : sql server
select top 3
    column_name
from table_name

-- percent : sql server
SELECT top 50 percent
    column_name
from table_name

-- limit : mysql
select *
from table_name limit
3;

-- rownum: oracle
select * from table_name where rownum >= 1

-- min, max, count, avg, sum
select min(column_name) from table_name
select max(column_name) from table_name
select count(column_name) from table_name
select avg(column_name) from table_name
select sum(column_name) from table_name

-- insert into 
insert into table_name
    (column1, column2)
VALUES
    (value_1, value_2);

insert into table_name
VALUES
    (value_1, value_2, ..., value_n);

-- null, not null
select *
from table_name
where column1 is null;

select column1, column2
from table_name
where column3 is not null;

-- update
update table_name
set column1 = 'value1', column2='value2'
where condition;

-- delete
delete from table_name where condition;
