import random


def generate_password():

    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*"

    characters = lowercase + uppercase + numbers + symbols

    try:
        length = int(input("Enter password length: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if length < 4:
        print("Password length must be at least 4.")
        return

    password = ""

    # Guarantee one character from each category
    password += random.choice(lowercase)
    password += random.choice(uppercase)
    password += random.choice(numbers)
    password += random.choice(symbols)

    # Generate remaining characters
    remaining = length - 4

    for i in range(remaining):
        password += random.choice(characters)

    # Shuffle the password
    password_list = list(password)
    random.shuffle(password_list)

    password = "".join(password_list)

    print("\nGenerated password:", password)


def check_password_strength():

    symbols = "!@#$%^&*"

    password = input("Enter your password: ")

    if password == "":
        print("Password cannot be empty.")
        return

    has_lowercase = False
    has_uppercase = False
    has_number = False
    has_symbol = False


    for char in password:

        if char.islower():
            has_lowercase = True

        if char.isupper():
            has_uppercase = True

        if char.isdigit():
            has_number = True

        if char in symbols:
            has_symbol = True

    print("\nPassword:", password)
    print("Lowercase:", has_lowercase)
    print("Uppercase:", has_uppercase)
    print("Number:", has_number)
    print("Special character:", has_symbol)

    if has_lowercase and has_uppercase and has_number and has_symbol:
        print("Strength: Strong")
    else:
        print("Strength: Weak")


while True:

    print("\n================================")
    print("       PASSWORD UTILITY")
    print("================================")
    print("1. Generate Password")
    print("2. Check Password Strength")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        generate_password()

    elif choice == "2":

        check_password_strength()

    elif choice == "3":

        print("Goodbye!")
        break

    else:

        print("Invalid choice. Please try again.")