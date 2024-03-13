SELECT sub.name AS subject_name
FROM subjects sub
JOIN teachers t ON sub.teacher_id = t.id
-- Вкажіть ім'я викладача
WHERE t.name = 'Tammy Boyd';