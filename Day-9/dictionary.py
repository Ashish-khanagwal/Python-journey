# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

programming_dictionary = {
  "bug": "An error in a program that prevents the program from running as expected",
  "function": "A piece of code that you can easily call over and over again"
}

# here, "bug" and "function" are KEYs and data provided to these keys are VALUEs, and 
# combined they are known as KEY-VALUE pair

# Retrieving items from dictionary, This is how we can derive any value from a dictionary
# by calling it with their keys.
# print(programming_dictionary["bug"])

# Adding new items to the dictionary
programming_dictionary["loop"] = "The action of doing something over and over again."
# print(programming_dictionary)

# wiping out whole dictionary
programming_dictionary = {} # => Now, we will get the empty dictionary
print(programming_dictionary)