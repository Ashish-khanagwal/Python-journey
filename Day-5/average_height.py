student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
    total_height += height

num_of_stu = 0
for student in student_heights:
    num_of_stu += 1

average_height = total_height / num_of_stu
print(round(average_height))

# we can achieve the same result with just 2-3 lines of code.

total = sum(student_heights) # we use sum to get the total of list.
num = len(student_heights)
average = total / num
print(round(average))