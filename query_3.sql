SELECT g.name AS group_name, AVG(gg.grade) AS avg_grade
FROM groups g
JOIN students s ON g.id = s.group_id
JOIN grades gg ON s.id = gg.student_id
JOIN subjects sub ON gg.subject_id = sub.id
-- Вкажіть назву предмета
WHERE sub.name = 'good'
GROUP BY g.id;
