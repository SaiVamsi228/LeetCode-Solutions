SELECT E1.employee_id, E1.name, COUNT(E2.reports_to) as reports_count, ROUND(AVG(E2.age)) as average_age
FROM Employees E1
JOIN Employees E2
ON E1.employee_id = E2.reports_to
GROUP BY E1.employee_id
ORDER BY E1.employee_id;