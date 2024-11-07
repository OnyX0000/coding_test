# Write your MySQL query statement below
SELECT b.name
FROM Employee a
INNER JOIN Employee b on a.managerId = b.id
GROUP BY a.managerId 
HAVING COUNT(a.id) >= 5