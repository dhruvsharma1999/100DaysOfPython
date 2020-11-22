#Tip calculator program 
print("Welcome to the tip calculator.")

#input the amount of the bill
bill = float(input("What is the total bill amount? $"))
tip = int(input("How much tip would you like to give? 10, 12, 15? "))
people = int(input("How many people to split the bill? "))

bill_with_tip = bill * (1 + tip/100)
amount_each = int(bill_with_tip / people)
final_amount = round(amount_each, 2)

#using literal string interpolation / F-strings
print(f"Amount each person has to pay: {final_amount}$") 