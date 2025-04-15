import customtkinter as ctk
import random

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
special_characters = '!@#$%^&*()-_=+[]{};:,.<>?/|`~'


def generate_password_gui():
    # If the user enters a non-integer value, it will show an error message in the password field
    try:
        # Get the number of letters, numbers, and symbols from the user input
        num_letters = int(entry_letters.get())
        num_numbers = int(entry_numbers.get())
        num_symbols = int(entry_symbols.get())

        
        total = [] # List to store the password to be generated

        # For loop to add letters, numbers, and symbols to the password
        for i in range(num_letters): 
            total.append(random.choice(letters))
        for i in range(num_numbers):
            total.append(random.choice(numbers))
        for i in range(num_symbols):
            total.append(random.choice(special_characters))

        random.shuffle(total)
        password = ''.join(total)

        entry_result.delete(0, ctk.END)
        entry_result.insert(0, password)
    except ValueError:
        entry_result.delete(0, ctk.END)
        entry_result.insert(0, "Enter valid numbers")


# Set up the appearance and theme
ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("blue")  

# Creates the app window
app = ctk.CTk()
app.geometry("400x400")
app.title("Password Generator")

# Input box: Number of Letters
ctk.CTkLabel(app, text="Enter Number of Letters:").pack(pady=5)
entry_letters = ctk.CTkEntry(app)
entry_letters.pack(pady=5)

# Input box: Number of Numbers
ctk.CTkLabel(app, text="Enter Number of Numbers:").pack(pady=5)
entry_numbers = ctk.CTkEntry(app)
entry_numbers.pack(pady=5)

# Input box: Number of Special Characters
ctk.CTkLabel(app, text="Enter Number of Special Characters:").pack(pady=5)
entry_symbols = ctk.CTkEntry(app)
entry_symbols.pack(pady=5)

# Output box: Display Password
ctk.CTkLabel(app, text="Your Password").pack(pady=(15, 5))
entry_result = ctk.CTkEntry(app, width=300)
entry_result.pack(pady=5)

# Button: Generates Password
generate_button = ctk.CTkButton(app, text="Generate Password", command=generate_password_gui)
generate_button.pack(pady=20)
