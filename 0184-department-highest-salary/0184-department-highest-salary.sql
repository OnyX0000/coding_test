# Write your MySQL query statement below
SELECT 
    d.name as Department,
    e.name as Employee,
    e.salary
FROM Department d
JOIN Employee e on e.departmentId = d.id 
WHERE (departmentId, salary) in (SELECT departmentId, MAX(salary) FROM Employee GROUP BY departmentId)