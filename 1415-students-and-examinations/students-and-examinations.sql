


SELECT comb.student_id, comb.student_name, comb.subject_name, IFNULL(cnt_frq.attended_exams, 0) AS attended_exams
FROM 

(SELECT s.student_id, s.student_name, sb.subject_name
FROM Students s
CROSS JOIN Subjects sb
ORDER BY student_id, student_name, subject_name) AS comb

LEFT JOIN

(SELECT student_id, subject_name, COUNT(subject_name) as attended_exams
FROM Examinations
GROUP BY student_id,subject_name
ORDER BY student_id) AS cnt_frq

ON comb.student_id = cnt_frq.student_id AND comb.subject_name = cnt_frq.subject_name
GROUP BY comb.student_id, comb.student_name, comb.subject_name
ORDER BY comb.student_id, comb.student_name, comb.subject_name;



