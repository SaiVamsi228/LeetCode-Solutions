SELECT E.name 
from Employee E
RIGHT JOIN
(SELECT managerId,COUNT(managerId) AS report_freq
FROM Employee
GROUP BY managerId) AS R 
ON E.id = R.managerId
WHERE R.report_freq >= 5 AND R.managerId IS NOT NULL AND E.id IS NOT NULL;