import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = [rock, paper, scissors]
user_choose = int(input(
    "What do you choose? Type 0 for Rock. 1 for paper or 2 for Scissors "))
if user_choose >= 3 or user_choose < 0:
  print("You typed an invalid number, you lose")
else: 
  print("You chooses:")
  user = print(choice[user_choose])
  
  print("Computer choose:")
  comp_choose = random.randint(0, len(choice) - 1)
  comp = print(choice[comp_choose])
  
  if user_choose == 0 and comp_choose == 2:
    print("You win")
  elif comp_choose == 0 and user_choose == 2:
    print("You loose")
  elif comp_choose > user_choose:
    print("You lose")
  elif comp_choose < user_choose:
    print("You win")
  else:
    print("Match draw")