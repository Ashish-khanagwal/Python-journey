print("Welcome to Treasure Island. You mission is to find the treasure.")
print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
path = input("In what direction you want to go? Left or Right: ")
l_path = path.lower()
if l_path == 'left':
  way = input("Hey, found a island, do you want to wait or swim? ")
  l_way = way.lower()
  if l_way == 'wait':
    door = input("from which door you want to enter? Red, Yellow, or Blue: ")
    l_door = door.lower()
    if l_door == 'yellow':
      print("huraay! you found the treasure.")
    elif l_door == 'red':
      print("ohhh! you burned by fire. Game over!")
    elif l_door == "blue":
      print("oops! you eaten by beasts, Game over!")
    else:
      print("wrong move, Game over!")
  else:
    print("You are under attack, oh no! killed by trouts. Game over!")
else:
  print("hehe, you fallen into hole. Game over!")