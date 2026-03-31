# Write your MySQL query statement below
SELECT en.unique_id,e.name
from employees e
left join
employeeUni en
on
e.id=en.id