# Write your MySQL query statement below


select ifnull(
(select a.salary as s from (select salary, dense_rank() over (order by salary desc) as ranked from Employee) a where ranked = 2 limit 1), null) as SecondHighestSalary;