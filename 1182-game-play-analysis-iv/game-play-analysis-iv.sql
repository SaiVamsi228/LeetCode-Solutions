SELECT ROUND(COUNT(A.player_id)/(SELECT COUNT(DISTINCT player_id) FROM Activity),2) AS fraction
FROM
(SELECT player_id, MIN(event_date) as first_login
FROM Activity
GROUP BY player_id) AS A
INNER JOIN
Activity P
ON A.player_id = P.player_id AND P.event_date = A.first_login + INTERVAL 1 DAY;
