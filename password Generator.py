import random
import string

def generate_password(length, complexity):
    if complexity == '1':
        characters = string.ascii_letters  # Only letters (lowercase and uppercase)
    elif complexity == '2':
        characters = string.ascii_letters + string.digits  # Letters and numbers
    elif complexity == '3':
        characters = string.ascii_letters + string.digits + string.punctuation  # Letters, numbers, and punctuation
    else:
        return "Invalid complexity choice. Please choose 1, 2, or 3."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator():
    print("Password Generator")
    length = int(input("Enter the desired length of the password: "))
    complexity = input("Enter the desired complexity (1 for letters, 2 for letters and numbers, 3 for letters, numbers, and punctuation): ")

    password = generate_password(length, complexity)
    print(f"Generated Password: {password}")

# Run the password generator
password_generator()
