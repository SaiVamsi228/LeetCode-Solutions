SELECT DISTINCT P1.email
FROM Person P1
JOIN
Person P2
ON P1.id != P2.id and P1.email = P2.email;


