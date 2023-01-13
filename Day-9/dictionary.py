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
# programming_dictionary = {} # => Now, we will get the empty dictionary
# print(programming_dictionary)

# Editing an item in a dictionary
programming_dictionary["bug"] = "A moth in your computer."
# print(programming_dictionary)

# Loop through a dictionary
for key in programming_dictionary:
  print(key) # It'll print out the keys only, instead of printing the whole key-value pair
  print(programming_dictionary[key]) # It'll print out the values only, instead of printing the whole key-value pair

# List in a dictionary
travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

# Dictionary in a dictionary
travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany" : {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}
}

# Nesting a dictionary in a list
travel_log = [
  {
    "country": "France", 
    "cities_visited" : ["Paris", "Lille", "Dijon"],
    "total_visits": 12
  },
  {
    "country": "Germany", 
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
    "total_visits": 5
  }
]