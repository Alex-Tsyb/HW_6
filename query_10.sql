SELECT DISTINCT sub.name AS subject_name
FROM subjects sub
JOIN grades g ON sub.id = g.subject_id
JOIN students s ON g.student_id = s.id
JOIN teachers t ON sub.teacher_id = t.id
-- Вкажіть ім'я студента та ім'я викладача
WHERE s.name = 'Marissa Mercer' AND t.name = 'Tammy Boyd';