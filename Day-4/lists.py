list = "ashish"

# LISTS: Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
# Lists are created using square brackets:

states_of_india = ["Jammu", "Kashmir", "Himachal pradesh", "Haryana", "Punjab", "Rajasthan", "Gujarat", "Uttar pradesh"]
print(states_of_india[1]) # In list indexing starts from '0'. So, here if we call for '1', Kashmir will return.

# we also can change value at an partcular index, like if we want to change value of index no. 3 then, simply do this
states_of_india[3] = "Assam"
print(states_of_india[3]) # you'll find instead of printing "Haryana", it will return "Assam", because we overwrited it.

# If we want to return value from the last, then we will specify negative indexing and it starts from [-1] => "Uttar pradesh" as of present list seneraio.
print(states_of_india[-1])

# we can use Append() to insert value at the end of the list.
states_of_india.append("Maharashtra")
print(states_of_india)

# If you want to explore more about lists then do follow the python's documentation.
states_of_india.remove("Punjab") # it will remove the specified value from the list
print(states_of_india) 

# we can directly convert string innto a list by separating out the commas using str.split(',')
str_inp = "Ashish,From,India"
li = str_inp.split(",") # By using this method, we can easily convert string into list 
print(li)

# INDEXERROR: Index out of range error --> This error occurs due to when we try to access any element beyond the range of list/sequece
num_len = len(states_of_india)
print(num_len)
# print(states_of_india[num_len]) # this will give us an error of Indexerror

print(states_of_india[num_len - 1]) # To avoid this error.

# dirty_dozen = ["Strawberry", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
# there's a term called Nested list

fruits = ["Strawberry", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables] # This list contains further two lists and this is called nested list
print(dirty_dozen)