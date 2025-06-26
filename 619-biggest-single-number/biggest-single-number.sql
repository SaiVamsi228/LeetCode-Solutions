# Write your MySQL query statement below
SELECT IF(COUNT(num) != 0,MAX(num),NULL) AS num
FROM MyNumbers
WHERE num IN (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(num) = 1
);