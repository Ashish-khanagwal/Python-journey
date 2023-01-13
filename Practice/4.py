str = input("Enter a string\n")
words = input("How many letter you want to remove? ")

def remove_letter(word, num):
  print(word[num:])
remove_letter(word=str, num=words)