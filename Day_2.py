# Tip Calculator

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_as_percentage = tip/100
tip_total = bill * tip_as_percentage
total_bill = bill + tip_total
share = total_bill / people
final_amount = round(share, 2)
print(f"Each share is {final_amount}")