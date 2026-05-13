# Tip Calculator

# Display a welcome message to the user
print("Welcome to the tip calculator!")

# Ask the user for the total bill amount
bill = float(input("What was the total bill? $"))

# Ask the user for the tip percentage
tip = int(input("What percentage tip would you like to give? 10 12 15 "))

# Ask how many people will split the bill
people = int(input("How many people to split the bill? "))

# Convert the tip percentage into a decimal
tip_as_percentage = tip / 100

# Calculate the total tip amount
tip_total = bill * tip_as_percentage

# Add the tip to the original bill
total_bill = bill + tip_total

# Divide the total bill by the number of people
share = total_bill / people

# Round the final amount to 2 decimal places
final_amount = round(share, 2)

# Display the amount each person should pay
print(f"Each share is ${final_amount}")