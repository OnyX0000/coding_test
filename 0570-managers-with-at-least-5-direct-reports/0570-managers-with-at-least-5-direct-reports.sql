# Write your MySQL query statement below
SELECT b.name
FROM Employee as a
INNER JOIN Employee as b on a.managerId = b.id
GROUP BY a.managerId 
HAVING COUNT(a.id) >= 5