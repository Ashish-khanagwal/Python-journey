student_heights = input("Enter the height of students: ").split(", ")
for n in range(0, (len(student_heights))):
  student_heights[n] = int(student_heights[n])

total_height = 0
for h in student_heights:
  total_height += h
print(total_height)

no_of_students = 0
for student in student_heights:
  no_of_students += 1

average_height = round(total_height / no_of_students)
print(average_height)