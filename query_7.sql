SELECT s.name AS student_name, g.grade
FROM students s
JOIN grades g ON s.id = g.student_id
JOIN subjects sub ON g.subject_id = sub.id
JOIN groups gr ON s.group_id = gr.id
-- Вкажіть назву предмета та назву групи
WHERE sub.name = 'good' AND gr.name = 'B';