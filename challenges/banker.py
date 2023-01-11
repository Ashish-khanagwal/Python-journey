import random

names_string = "Ashish, Manish, Lalit, Saurav"
names_list = names_string.split(", ")
ran_name = random.randint(0, (len(names_list)-1))
print(f"{names_list[ran_name]} is going to buy the meal today!")