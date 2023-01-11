import random

from hangman_words import word
from hangman_art import logo, stages

chosen_word = random.choice(word)
word_length = len(chosen_word)
print(chosen_word)

display = []
for i in range(word_length):
    display += "_"
print(display)

end_of_game = False
lives = 6

print(logo)

while not end_of_game:
  guess =  input("Guess a letter: ").lower()

  if guess in display:
    print(f"You have already guessed {guess}")

  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter

  if guess not in chosen_word:
    print(f"You guessed {guess}, that's not in the word. You lose a life.")
    lives -= 1
    if lives == 0:
      end_of_game = True
      print("You lose.")

  print(f"{' '.join(display)}")

  if "_" not in display:
    end_of_game = True
    print("You win.")
  
  print(stages[lives])