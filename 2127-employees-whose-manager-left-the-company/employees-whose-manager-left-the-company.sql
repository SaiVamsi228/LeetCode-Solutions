SELECT 
    employee_id
FROM    
    Employees
WHERE
    salary < 30000
AND
    manager_id
NOT IN
    (
        SELECT 
            E1.employee_id
        FROM 
            Employees E1
        JOIN
            Employees E2
        ON
            E1.employee_id = E2.manager_id
    )
ORDER BY 
    employee_id;