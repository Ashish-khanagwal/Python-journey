print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("Hurayy! you can ride the rolercoaster")
  age = int(input("What is your age? "))
  if age <= 12:
    bill = 5
    print("Child tickets are $5.")
  elif 12 < age < 18:
    bill = 7
    print("Yoith tickets are $7.")
  else:
    bill = 15
    print("Adult tickets are $15.")
  photo = input("Do you want a photo? Y or N: ")
  if photo == "Y":
    bill += 3
  print(f"you total bill is ${bill}")
else:
  print("Sorry, you're not tall enough to ride the rollercoaster")