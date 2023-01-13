sum_now = 0
for i in range(1, 11):
  sum_nxt = sum_now + i
  print(f"current number{i} previous number {sum_now} Sum: {sum_nxt} ")
  sum_now = i