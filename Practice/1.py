def calc(num1, num2):
  product = num1*num2
  if product >= 1000:
    print(f"The product of theses numbers is {product} ")
  else:
    print(f"The sum of theses numbers is {num1+num2} ")

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
calc(num1, num2)