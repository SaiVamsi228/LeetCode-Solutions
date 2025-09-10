# Write your MySQL query statement below
SELECT product_name, unit 
FROM (SELECT P.product_name as product_name,  SUM(O.unit) as unit
FROM Products P
JOIN 
Orders O
ON P.product_id = O.product_id
WHERE MONTH(O.order_date) = 2 AND YEAR(O.order_date) = 2020
GROUP BY O.product_id
HAVING unit >= 100) AS t;