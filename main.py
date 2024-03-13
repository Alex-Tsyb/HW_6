from faker import Faker
import sqlite3
import random
import os

fake = Faker()

# Створення з'єднання з базою даних
conn = sqlite3.connect('university.db')
cursor = conn.cursor()

# Створення таблиць
cursor.execute('''CREATE TABLE students (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    group_id INTEGER
                )''')

cursor.execute('''CREATE TABLE groups (
                    id INTEGER PRIMARY KEY,
                    name TEXT
                )''')

cursor.execute('''CREATE TABLE teachers (
                    id INTEGER PRIMARY KEY,
                    name TEXT
                )''')

cursor.execute('''CREATE TABLE subjects (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    teacher_id INTEGER
                )''')

cursor.execute('''CREATE TABLE grades (
                    id INTEGER PRIMARY KEY,
                    student_id INTEGER,
                    subject_id INTEGER,
                    grade INTEGER,
                    date TEXT
                )''')

# Заповнення таблиць випадковими даними
# Додамо 3 групи
for group_name in ["A", "B", "C"]:
    cursor.execute("INSERT INTO groups (name) VALUES (?)", (group_name,))

# Додамо 5-8 предметів і 3-5 викладачів
for i in range(1, random.randint(3, 6)):
    cursor.execute("INSERT INTO teachers (name) VALUES (?)", (fake.name(),))

# Отримаємо список усіх викладачів
cursor.execute("SELECT id FROM teachers")
teachers = cursor.fetchall()

# Додамо випадкову кількість предметів для кожного викладача
for teacher_id in teachers:
    # Генерація випадкової кількості предметів для кожного викладача у межах від 1 до 8
    num_subjects = random.randint(1, min(8, random.randint(1, 5)))  # Обмеження максимальною кількістю предметів
    for _ in range(num_subjects):
        # Генерація випадкової назви предмету
        subject_name = fake.word()
        # Додавання предмету до таблиці
        cursor.execute("INSERT INTO subjects (name, teacher_id) VALUES (?, ?)",
                       (subject_name, teacher_id[0]))

# Додамо 30-50 студентів
for i in range(1, random.randint(30, 50)):
    cursor.execute("INSERT INTO students (name, group_id) VALUES (?, ?)", (fake.name(), random.randint(1, 3)))

# Отримання списку усіх студентів
cursor.execute("SELECT id FROM students")
students = cursor.fetchall()

# Отримання кількості предметів
cursor.execute("SELECT COUNT(*) FROM subjects")
num_subjects = cursor.fetchone()[0]

# Додавання оцінок для кожного студента
for student_id in students:
    # Генерація випадкової кількості оцінок для кожного студента на основі кількості предметів
    num_grades = random.randint(1, num_subjects * 4)  # Множимо на 4, щоб кількість оцінок була відносно невеликою
    for _ in range(num_grades):
        # Генерація випадкової оцінки та дати
        subject_id = random.randint(1, num_subjects)  # Виберемо випадковий предмет
        grade = random.randint(1, 100)
        date = fake.date()
        # Додавання оцінки до таблиці
        cursor.execute("INSERT INTO grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)",
                       (student_id[0], subject_id, grade, date))


# Збереження змін до бази даних
conn.commit()
conn.close()

