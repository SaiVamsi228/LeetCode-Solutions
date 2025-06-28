SELECT
    modified.person_name
FROM
    (SELECT 
        turn, person_id, person_name, weight, 
        SUM(weight) OVER (ORDER BY turn) AS running_total
    FROM
        Queue) as modified
WHERE modified.running_total <= 1000
ORDER BY turn DESC LIMIT 1;