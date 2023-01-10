print("Welcome to the rollercoaster!")
height = int(input("Enter your height (in cm) "))
bill = 0

if height >= 120:
  print("Hurray! you can ride the rollercoaster ")
  age = int(input("Enter your age "))
  if age < 12:
    bill = 5
    print("you have to pay $5")
  elif age >= 12 and age <= 18:
    bill = 7
    print("you have to pay $7")
  else:
    bill = 10
    print("you have to pay $10")
  photo = input("Do you want a photo? Y or N ")
  if photo == "Y":
    bill += 3
  print(f"Your total bill is ${bill}")
else:
  print("Sorry, you can't ride the rollercoaster")