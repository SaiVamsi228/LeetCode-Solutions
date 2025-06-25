SELECT product_id, IFNULL(ROUND(IFNULL(SUM(joined_data.price * joined_data.units),0)/IFNULL(SUM(joined_data.units),1),2),0) AS average_price FROM
(SELECT Prices.product_id ,Prices.start_date ,Prices.end_date,Prices.price,SUM(UnitsSold.units) AS units
FROM Prices
LEFT JOIN UnitsSold 
ON Prices.product_id = UnitsSold.product_id AND purchase_date BETWEEN Prices.start_date AND Prices.end_date
GROUP BY Prices.product_id,Prices.start_date, Prices.end_date, Prices.price) AS joined_data
GROUP BY product_id