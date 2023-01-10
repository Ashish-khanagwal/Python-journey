print("Welcome to the love calculator")
name1 = input("Enter your name ")
name2 = input("Enter your soulmate name ")
whole_name = (name1 + name2).casefold()
print(whole_name)
t = whole_name.count("t")
r = whole_name.count("r")
u = whole_name.count("u")
e = whole_name.count("e")
true = t + r + u + e
l = whole_name.count("l")
o = whole_name.count("o")
v = whole_name.count("v")
e = whole_name.count("e")
love = l + o + v + e
love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
  print(f"Your love score is {love_score}, you go together like coke and mentos")
elif (love_score >= 40) and (love_score <= 50):
  print(f"Your love score is {love_score}, you are alright together")
else:
  print(f"Your love score is {love_score}")
