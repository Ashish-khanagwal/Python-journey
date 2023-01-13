student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for key in student_scores:
    values = student_scores[key]
    if values >= 91 and values <= 100:
        student_grades[key] = "Outstanding"
    elif values >= 81 and values <= 90:
        student_grades[key] = "Exceeds Expectatios"
    elif values >= 71 and values <= 80:
        student_grades[key] = "Acceptable"
    elif values <= 70:
        student_grades[key] = "Fail"

print(student_grades)