str = input("Enter a string\n")
words = int(input("How many letter you want to remove? "))

def remove_chars(str, words):
  rem_str = ""
  rem_str += str[words:]
  print(f"remaining string is {rem_str} ")

remove_chars(str, words)