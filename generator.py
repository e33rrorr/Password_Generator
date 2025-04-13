import random

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' # All letters (lowercase + uppercase)
numbers = '0123456789'
special_characters = '!@#$%^&*()-_=+[]{};:,.<>?/|`~' # All special characters 

print("---Welcome to the Password Generator!---")
number_of_letters = int(input("Enter the number of letters you would like: "))
number_of_numbers = int(input("Enter the number of numbers you would like: "))
number_of_special_characters = int(input("Enter the number of special characters you would like: "))

total = [] # List to store the password to be generated

for i in range(number_of_letters): # Loop to add letters to the password
    total.append(random.choice(letters)) # Append a random letter to the password
for i in range(number_of_numbers): # Loop to add numbers to the password
    total.append(random.choice(numbers)) # Append a random number to the password
for i in range(number_of_special_characters): # Loop to add special characters to the password
    total.append(random.choice(special_characters)) # Append a random special character to the password

random.shuffle(total) # Shuffle the password to make it more secure

password = ''.join(total) # Join the list to make it a string

print(f"Your password is: {password}") # Print the password
