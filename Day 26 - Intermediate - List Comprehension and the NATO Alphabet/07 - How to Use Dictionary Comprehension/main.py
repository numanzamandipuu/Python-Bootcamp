import random

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

students_score = {s : random.randint(1, 100) for s in names}
print(students_score)

passed_students = {students : score for (students, score) in students_score.items() if score >= 60}
print(passed_students)