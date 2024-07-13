import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_passwords(number, length):
    return [generate_password(length) for _ in range(number)]

def main():
    print("Welcome to the Password Generator!")
    
    while True:
        try:
            length = int(input("Enter the length of the password: "))
            if length < 8:
                print("Password length should be at least 8 characters for security.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    while True:
        try:
            number = int(input("Enter the number of passwords to generate: "))
            if number < 1:
                print("You must generate at least one password.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    passwords = generate_passwords(number, length)
    for i, password in enumerate(passwords, 1):
        print(f"Password {i}: {password}")

if __name__ == "__main__":
    main()
