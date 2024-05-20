# Write your MySQL query statement below
DELETE p2 
FROM Person p1, Person p2
WHERE p1.Email = p2.Email and p2.id > p1.id