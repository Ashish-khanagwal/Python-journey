print("Welcome to Apna Zayka Pizza Hub")
size = input("What size pizza do you want? S, M, or L ").upper()
bill = 0

if (size == "S"):
  bill = 15
elif (size == "M"):
  bill = 20
else:
  bill = 25
add_pep = input("Do you want pepperoni? Y or N ").upper()
if (add_pep == "Y" and size == "S"):
  bill += 2
elif (add_pep == "Y" and (size == "M" or size == "L")):
  bill += 3
extra_cheese = input("Do you want extra chesse? 'Y' or 'N'").upper()
if (extra_cheese == "Y"):
  bill += 1
print(f"Your final bill is ${bill}")