num = input("Enter the numbers: ")
num_list = num.split(", ")
for i in range(len(num_list)-1):
  num_list[i] = int(num_list[i])
