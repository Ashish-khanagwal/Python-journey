# We will built a simple rollercoaster height check program
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

# when we use [=] it means we're assigning some value to a variable
# and when we use [==] it means we're checking for equality

if height >= 120:
  print("Hurayy! you can ride the rolercoaster")
  age = int(input("What is your age? "))
  if age < 12:
    print("You have to pay $5")
  elif 12 < age < 18:
    print("You have to pay $7")
  else:
    print("You have to pay $15")
else:
  print("Sorry, you're not tall enough to ride the rollercoaster")