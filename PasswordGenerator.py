import random
import string

# we create a function that accepts three parameters


def generate_password(min_length, numbers=True, special_characters=True):
    # This grabs all letters that we have in the English languate
    letters = string.ascii_letters
    digits = string.digits  # Grabs the digits 1-9
    special = string.punctuation  # Grabs all special characters

    # we create a string that contains all of the different characters we could select from
    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    # we set pwd which is the password to empty string
    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    # we make a while loop
    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd


min_length = int(input("Enter the minimum length: "))
has_number = input("Do you want to have numbers (y/n)? ").lower() == 'y'
has_special = input(
    "Do you want to have special characters (y/n)? ").lower() == 'y'
pwd = generate_password(min_length, has_number, has_special)
print("The generated password is:", pwd)
