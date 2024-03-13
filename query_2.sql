SELECT s.name AS student_name, AVG(g.grade) AS avg_grade
FROM students s
JOIN grades g ON s.id = g.student_id
JOIN subjects sub ON g.subject_id = sub.id
-- Вкажіть назву предмета
WHERE sub.name = 'good'
GROUP BY s.id
ORDER BY avg_grade DESC
LIMIT 1;