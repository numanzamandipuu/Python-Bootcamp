student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.

student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇

for dictionary in student_scores:
    if student_scores[dictionary] > 90:
        student_grades[dictionary] = "Outstanding"
    elif student_scores[dictionary] > 80:
        student_grades[dictionary] = "Exceeds Expectations"
    elif student_scores[dictionary] > 70:
        student_grades[dictionary] = "Acceptable"
    elif student_scores[dictionary] <= 70:
        student_grades[dictionary] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)