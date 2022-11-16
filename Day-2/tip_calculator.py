total_bill = input("What was the total bill : $")
bill_tip = input("What percentage would you like to give? 10, 12, or 15? ")
bill_split = input("how many people to split the bill? ")

Bill_pay = ((float(total_bill) / int(bill_split)) * ((int(bill_tip)/100)+1))

# For more precise value, we should use precision round off method instead of using simple round off method.
# Pay = (round(Bill_pay, 2))
final_pay = "{:.2f}".format(Bill_pay) # this will give exact value 
print(f"Each person should pay: ${final_pay}")