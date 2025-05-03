# importing the necessary libraries
import string
import random
import re
from traceback import TracebackException

# the password generator
def generate_password():
    print("\nPassword generator...")
    try:
        length = input("Enter desired password length: ") # prompts for password length and handles keyboardinterrupt error
    except KeyboardInterrupt: #
        print("\n\nStopping program...")
        exit()

    # check if the input is a number and more than 8 characters
    try:
        length = int(length)
        while True:
            if length < 8: # check if the length is less than 8 and prompt for input again
                print("\nPassword length must be at least 8 characters.")
                length = input("Enter desired password length: ")
                length = int(length)
            else:
                break
    except ValueError: # handles the case where the input is not a number
        print("Invalid input. Please enter a number.")
        return
    except KeyboardInterrupt:
        print("\n\nStopping program...")
        exit()

    # define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    print("\nGenerated password: " + password)

# the password strength checker
def strength_password():
    print("\nPassword checker...")
    try:
        yourpassword = input("Enter your password: ") # prompts for password and handles keyboardinterrupt error
    except KeyboardInterrupt:
        print("\n\nStopping program...")
        exit()

    # check if the password is empty
    try:
        if not yourpassword:
            raise ValueError("\nPassword cannot be empty.")
    except ValueError as e:
        print(e)
        return

    # password criteria checker
    errors = [] # list to store errors, initialized as empty
    if len(yourpassword) < 8:
        errors.append("Password must be at least 8 characters long.")
    if not re.search("[a-z]", yourpassword):
        errors.append("Password must contain at least one lowercase letter.")
    if not re.search("[A-Z]", yourpassword):
        errors.append("Password must contain at least one uppercase letter.")
    if not re.search("[0-9]", yourpassword):
        errors.append("Password must contain at least one digit.")
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", yourpassword):
        errors.append("Password must contain at least one special character.")
    else:
        print("\nPassword is strong!")
        return
    if errors: # if there are errors, print them
        print("\nPassword is weak. Please consider the following suggestions:")
        for error in errors:
            print(f"- {error}")

# the menu
print("Welcome to my password generator / checker!\n")
print("1. Generate a password\n2. Check a password's strength\n3. Exit")

# prompts for choice, handles keyboardinterrupt error
try:
    choice = input("\nChoose an action: ")
except KeyboardInterrupt:
    print("\n\nStopping program...")
    exit()

# handles the choice
if choice == '1':  # the password generator
    generate_password()
elif choice == '2':  # the password strength checker
    strength_password()
elif choice == '3':  # exit
    print("\nExiting...")
    exit()
else:  # invalid choice
    print("\nInvalid choice. Please try again.")