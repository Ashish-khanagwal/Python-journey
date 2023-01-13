str = input("Enter a string ")
length = len(str)

def even_index(word):
  for index in range(length-1):
    if index % 2 == 0:
      print(word[index])

even_index(word=str)