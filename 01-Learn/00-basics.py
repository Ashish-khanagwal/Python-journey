print("Hello world")
name = "Ashish"
print(name)

full_name = "Ashish khanagwal"
width, height = 500, 1000
print(width, height)

your_name = input("Enter your name: ")
print(your_name)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(num1 + num2)

###################### TIP CALCULATOR ######################
print("Thanks for ordering the food")
food_amount = int(input("Enter amount of your ordered food: $"))
tip = int(input("Enter the tip percentage you wanna give 10%, 20%, 30%: "))
tip_percentage = tip /100
tip_amount = food_amount * tip_percentage
total_bill = food_amount + tip_amount
print("-------------------------------")
print(f"Food Amount: ${food_amount}")
print(f"Tip Amount: ${tip_amount}")
print(f"your total billi ${total_bill}")
print("-------------------------------")
