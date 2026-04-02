# Write your MySQL query statement below
select e1.name
From employee e1
Inner join employee e2
on e1.id=e2.managerId
GROUP BY e2.managerId
HAVING COUNT(e2.managerId)>=5