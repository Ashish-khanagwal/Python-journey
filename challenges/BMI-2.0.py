height = float(input("Enter the height in m: "))
weight = int(input("Enter the weight in kg: "))
BMI = weight // (height * height)

if (BMI < 18.5):
  print(f"Your BMI is {BMI}, you are underweight")
elif (BMI >= 18.5 and BMI <= 25):
  print(f"Your BMI is {BMI}, you have a normal weight")
elif (BMI >= 25 and BMI <= 30):
  print(f"Your BMI is {BMI}, you are slightly overweight")
elif (BMI >= 30 and BMI <= 35):
  print(f"Your BMI is {BMI}, you are obese")
else:
  print(f"Your BMI is {BMI}, you are clinically obese")