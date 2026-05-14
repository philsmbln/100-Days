# Random Password Generator

# Import the random module to generate random characters
import random

# List of letters that can be used in the password
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

# List of numbers that can be used in the password
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# List of symbols that can be used in the password
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Display a welcome message
print("Welcome to the PyPassword Generator!")

# Ask the user how many letters they want
nr_letters = int(input("How many letters would you like in your password?\n"))

# Ask the user how many symbols they want
nr_symbols = int(input("How many symbols would you like?\n"))

# Ask the user how many numbers they want
nr_numbers = int(input("How many numbers would you like?\n"))

# Create an empty list to store password characters
password_list = []

# Add random letters to the password list
for char in range(0, nr_letters):
    password_list += random.choice(letters)

# Add random symbols to the password list
for char in range(0, nr_symbols):
    password_list += random.choice(symbols)

# Add random numbers to the password list
for char in range(0, nr_numbers):
    password_list += random.choice(numbers)

# Shuffle the list so the password characters appear randomly
random.shuffle(password_list)

# Create an empty string for the final password
password = ""

# Combine all characters in the list into a single string
for char in password_list:
    password += char

# Display the generated password
print(f"Your password is: {password}")