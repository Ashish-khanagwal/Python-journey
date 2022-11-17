# The canonical Pythonic way of doing this is

# >>> 'Kilometers'.lower()
# 'kilometers'
# However, if the purpose is to do case insensitive matching, you should use case-folding:

# >>> 'Kilometers'.casefold()
# 'kilometers'

# new = "Ashish".casefold()
# print(new)

# new_again = "Ashish".lower()
# print(next)

# we use count('letter you want to count') to count occurence of any letter.

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

names_together = name1 + name2
names_lower = names_together.lower()
t = names_together.count('t')
r = names_together.count('r')
u = names_together.count('u')
e = names_together.count('e')
true = t + r + u + e

l = names_together.count('l')
o = names_together.count('o')
v = names_together.count('v')
e = names_together.count('e')
love = l + o + v + e

score = int(str(true) + str(love))

if score <= 10 or score >= 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")