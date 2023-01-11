# print("Hello World")
# hello = input("What is your name: ")
# print("Hey " + hello)
# print(input("How are you? "))
# print("Thank you! What about you?\nI'm fine, thank you!")
# print(len(hello))

# length = str(len(input("What is your name? ")))
# print(type(length))

# print("hey! " + length + " Nice to see you here")

# score = 0;
# height = 1.80;
# isWinning = True;

# print(f"your score is {score}, your height is {height}, and you are winning {isWinning} ")

# name = input("What is your name? ")
# print(name.lower())

# names = "Ashish, Manish, Saurav, Lalit"
# print(names.split(","))
names = "Ashish, Parul, Sakshi, Manish, Saurav, Lalit"
names_list = names.split(", ")
print(names_list)
for i in names_list:
  print(i)

for a in range(0, 10):
  print(a)

num = 0
for h in range(0, 101):
  num += h
print(num)

fruit = ["Apple", "Banana", "Orange"]
for i in range(len(fruit)):
  print(fruit[i])
else:
  print("No more fruits")