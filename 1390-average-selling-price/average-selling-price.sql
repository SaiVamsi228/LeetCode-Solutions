SELECT P.product_id, IFNULL(ROUND(IFNULL(SUM(P.price * U.units),0)/IFNULL(SUM(U.units),1),2),0) AS average_price FROM
Prices P
LEFT JOIN UnitsSold U
ON P.product_id = U.product_id AND U.purchase_date BETWEEN P.start_date AND P.end_date
GROUP BY product_id;