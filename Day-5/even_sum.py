sum_even = 0
for a in range(1, 101):
    if a % 2 == 0:
        sum_even += a
print(sum_even)

# another way of finding sum between 1 and 100
total = 0
for b in range(2, 101, 2):
  total += b
print(total)