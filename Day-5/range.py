# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

for a in range(0, 10):
  print(a) # It will return 0 to 9, not 10

num = 0
for h in range(0, 101):
  num += h
print(num)

# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
for b in range(0, 21, 4): # here, it will get incremented by 4.
  print(b)