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

game_choices = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))


if user_choice >= 3 or user_choice < 0:
  print("You typed an invalid number, you lose!")
else:
  print(f" You chooses: {game_choices[user_choice]}")

  comp_choice = random.randint(0, (len(game_choices)-1))
  print(f"Computer chooses: {game_choices[comp_choice]}")

  if user_choice == 0 and comp_choice == 2 :
    print("you win!")
  elif user_choice == 2 and comp_choice == 0:
    print("You loose!")
  elif user_choice < comp_choice:
    print("You loose!")
  elif user_choice > comp_choice:
    print("You win")
  else:
    print("Match Draw!")