# Write your MySQL query statement below
SELECT S1.id, S2.student
FROM Seat S1
JOIN
Seat S2
ON
S1.id = S2.id + 1
AND 
S1.id % 2 = 0
UNION
SELECT S1.id, S2.student
FROM Seat S1
JOIN
Seat S2
ON
S1.id = S2.id - 1
AND 
S1.id % 2 = 1
UNION 
SELECT id, student
FROM Seat
WHERE id = (SELECT COUNT(*) FROM Seat ) 
AND id % 2 = 1
ORDER BY
id