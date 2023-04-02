############ If-Else statements ############
# score = int(input("Enter your exam score: "))
# if score >= 90:
#     print("You got A grade")
# elif score < 90 and score >= 80: 
#     print("You got B grade")
# elif score < 80 and score >=70:
#     print("You got C grade")
# elif score < 70 and score >=60:
#     print("You got D grade")
# else:
#     print("You got F grade")

############ Functions ############ 

'''
simple Greet message
'''
# def user_name(name):
#     print(f"Hello {name}")
# user_name(input("Enter your name: "))

'''
Takes 2 integer and returns their sum
>>> sum(1, 2)
3
'''
# def sum(num1, num2):
#     add = num1 + num2
#     return add

# a = int(input("Enter the first integer: "))
# b = int(input("Enter the second integer: "))
# print(sum(a, b))

'''
Conveting tip calculator from 00-basics.py
'''
# def tip_calc(food_amt, tip_perc):
#     tip = (tip_perc / 100) * food_amt
#     total_bill = food_amt + tip
#     return total_bill
# food_amt = float(input("Enter the food amount $: "))
# tip_perc = float(input("Enter your tip percentage %: "))
# print(tip_calc(food_amt, tip_perc))

'''
Weather to emoji function
'''
def weather_emoji(weather):
    if weather == "sunny" or  weather == "Sunny":
        emoji = "☀️"
    elif weather == "rainy" or  weather == "Rainy":
        emoji = "🌧"
    elif weather == "cloudy" or weather ==  "Cloudy":
        emoji = "☁️"
    elif weather == "snowy" or  weather == "Snowy":
        emoji = "❄️"
    else:
        emoji = "🤷‍♂️"
    return emoji

print(weather_emoji(input("Is the weather sunny, rainy, cloudy, snowy? ")))