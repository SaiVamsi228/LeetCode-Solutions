(SELECT DISTINCT product_id, 10 as price
FROM Products
WHERE product_id NOT IN
(SELECT DISTINCT product_id
FROM Products
where change_date <= '2019-08-16'
))
UNION
SELECT product_id, new_price as price
FROM Products P1
WHERE change_date in (
    SELECT MAX(P2.change_date)
    FROM Products P2
    WHERE P2.product_id = P1.product_id
      AND P2.change_date <= '2019-08-16'
    GROUP BY P2.product_id
);
