# we can create loops in python using For loop and While loop.
# The for loop is used to iterate over a collection of items such as Tuple, List, Set, Dictionary, String, etc.
# Python for loop is always used with the “in” operator.

# For loop syntax

# for element in sequence:
    # for statement code block
# else: # optional
    # else code block

fruits = ["Apples", "Banana", "Strawberry"]
for fruit in fruits:
  # for loop will run in a proper order, it will return fruit and then return fruits statement, Indentation is important
  print(fruit) # It will print every value of list 'fruits' one by one
  print(fruit + " pie")
  print(fruits) # It will return list fruits.
