import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# EASY PASSWORD

e_password = ""
for e in range(1, nr_letters + 1):
  e_password += random.choice(letters)
for e in range(1, nr_symbols + 1):
  e_password += random.choice(symbols)
for e in range(1, nr_numbers + 1):
  e_password += random.choice(numbers)
print(e_password)

# HARD PASSWORD

h_password = []
for h in range(1, nr_letters + 1):
  h_password.append(random.choice(letters))
for h in range(1, nr_symbols + 1):
  h_password.append(random.choice(symbols))
for h in range(1, nr_numbers + 1):
  h_password.append(random.choice(numbers))

print(h_password)
# Now, we have to shuffle the list and for that we will use an function, see below.
random.shuffle(h_password)
print(h_password)

# now we have to convert this shuffled list in string, see below

password = ""
for a in h_password:
  password += a
print(f"Your password is: {password}")