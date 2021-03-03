print("********************")
print("Welcome to Tip Calculator")
netBill = input("What is total bill? ")
percentage = input(
    "What percentage of bill would you like to give 10%, 12%, 15%, 20% ")
ppl = input("How many people to split the fare? ")
bill = float(netBill)+(float(netBill)*(int(percentage)/100))
print(f"Each Person should pay {round(bill/int(ppl),2)}")
print("********************")
