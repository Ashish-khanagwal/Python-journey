import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

li = len(names)

random_num = random.randint(0, li - 1)
payer = names[random_num]

print(payer + " is going to buy the meal today")

# Instead of writing this code, we can use --> random.choice(seq)
# This is a widely used function in practice, wherein you would want to randomly pick up an item from a List/sequence.

pay = random.choice(names) # It will do the same work as we did above, with that piece of code.
print(pay + " is goint to pay the bill") 