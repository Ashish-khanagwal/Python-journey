print('''
*******************************************************************************
          |                   |                  |                     |
__________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
__________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
__________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
way = input("You're at a crossroad, where do you want to go? Left or Right? ").lower()
if way == "left":
  sea_way = input("You've found yourself in ocean and saw a island, what do you want to do? Wait or Swim ").lower()
  if sea_way == "wait":
    color_way = input("What color do you want to choose? Red, Blue or Yellow? ").lower()
    if color_way == "yellow":
      print("Hurray! you've found the treasure")
    elif color_way == "red":
      print("ohhh! you've caught fire, burned and dead. Game Over!")
    elif color_way == "blue":
      print("huh! drowned in deep blue ocean and dead. Game Over!")
    else:
      print("Game Over!")
else:
  print("Game Over! You've fallen into a hole and dead.")