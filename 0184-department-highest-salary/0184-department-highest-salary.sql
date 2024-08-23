# Write your MySQL query statement below
SELECT 
    d.name as Department,
    e.name as Employee,
    Salary  
FROM Employee e
LEFT JOIN Department d on d.id = e.departmentId
WHERE (d.id, salary) in (SELECT d.id, MAX(salary) FROM Employee GROUP BY departmentId) 