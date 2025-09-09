-- # Write your MySQL query statement below
SELECT comb.student_id, comb.student_name, comb.subject_name, COUNT(E.subject_name) AS attended_exams
FROM 
(SELECT student_id, student_name, subject_name
FROM Students CROSS JOIN
Subjects) AS comb
LEFT JOIN
Examinations E
ON comb.student_id = E.student_id AND comb.subject_name = E.subject_name
GROUP BY comb.student_id, comb.student_name, comb.subject_name
ORDER BY student_id, subject_name;
