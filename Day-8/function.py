# Simple Function
def greet():
  print("Hello")
  print("Good evening!")
  print("Nice to see you!")

greet()

# Function which accepts 1 input

# def function(parameter):
#   Do something
# function(argument) => Calling a fucntion

name = input("What is your name? ")
def greet_again(name):
  print(f"Hello, {name}")
  print(f"Hope you're doing well, {name}")
greet_again(name)

# Function with more than 1 input
def details(name, location):
  print(f"My name is {name}")
  print(f"I live in {location}")

# These are called as postiotnal arguments
details("Ashish", "India")

# These are called as keyword arguments
details(location="India", name="Ashish")