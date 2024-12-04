import random
import string

def generate_password(length):
    # Define the characters to choose from: lowercase, uppercase, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    # Randomly select characters to form the password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the length of the password: "))
        if length < 6:
            print("Password length should be at least 6 characters for better security.")
        else:
            password = generate_password(length)
            print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()
