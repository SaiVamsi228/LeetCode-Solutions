SELECT DISTINCT Visits.CUSTOMER_ID AS CUSTOMER_ID, COUNT(CUSTOMER_ID) AS COUNT_NO_TRANS
FROM Visits 
WHERE Visits.visit_id NOT IN (SELECT Visits.visit_id 
FROM Visits
INNER JOIN Transactions
ON Visits.visit_id = Transactions.visit_id)
GROUP BY CUSTOMER_ID;