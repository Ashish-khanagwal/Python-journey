students_score = input("Enter the score of the students ").split(", ")
for n in range(0, len(students_score)):
  students_score[n] = int(students_score[n])
print(students_score)

high_score = 0
for score in students_score:
  if score > high_score:
    high_score = score
print(f"The highest score in the class is: {high_score}")