# Write your MySQL query statement below
SELECT distinct actor_id, director_id
FROM ActorDirector
WHERE (actor_id, director_id) in (SELECT actor_id, director_id 
                                  FROM ActorDirector 
                                  GROUP BY actor_id, director_id 
                                  HAVING COUNT(1) >= 3)