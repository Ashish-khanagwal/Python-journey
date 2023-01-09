# As we know, we use len function to print the lenght of the string.
print(len("Hello"))
# It will give us output as '5'.

# but when we use len fucntion like this:
# print(len(123456))
# here, we'll get some error, (TypeError: object of type 'int' has no len())

# DATA TYPES
# STRING: "Hello" : we can pull out one character from the whole string and this method is called Subscripting.

print("Hello"[0]) # It will return 'H' and we start counting from 0.
print("123" + "456") # Output: 123456 <= because they are still in quoted commas so, treated as String.

# INTEGER: 1235
print(123 + 456)

123_456_789 == 123456789

# FLOAT: 456.123
# BOOLEAN: True or False

## TYPE CHECK
num_char = len(input("What is your name? "))
print(num_char)

# print("Your name contains " + num_char + " characters")
# It will throw an error as we know, num_char is of integer type and it can't be concatinated as strings, so first we have to convert integer to String and this process is called Type Conversion.
new_num_char = str(num_char)

print("Your name contains " + new_num_char + " characters") # now it will work

print(type(num_char))
print(type(123))

# Rounding off in Python is easy

print(round(8 / 3)) # It will display 3 as output. We also can round off till an praticular place, see below
print(round(8 / 3, 2)) # it will round off till an 2nd decimal place

# As we know, if we'll perform an division then, it will return result as floating point number, but what if we want result as a Whole number.
print(8 // 3) # we'll do in this way, this is called floor division and it is of Integer type.

###########################################

score = 0;
height = 1.80;
isWinning = True;

# these all variables contains values of different data types and we want to store all those valuse in a string and want to diplay the result in form of a string.
# For doing this, we have to use type conversion for each and every data types present over here. There is one more we can achieve the same and this is called
### F - String

print(f"your score is {score}, your height is {height}, and you are winning {isWinning}")
# headache of manually type conversion is gone and we can use F-string instead.