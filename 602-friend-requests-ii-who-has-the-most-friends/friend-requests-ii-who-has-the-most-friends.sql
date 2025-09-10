# Write your MySQL query statement below
SELECT id, COUNT(id) as num
FROM 
(SELECT requester_id AS id FROM RequestAccepted 
UNION ALL 
SELECT accepter_id AS id FROM RequestAccepted) AS t1
GROUP BY id
ORDER BY num DESC LIMIT 1;
