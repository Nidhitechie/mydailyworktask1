import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        print("You must select at least one character type!")
        return ""

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")

    while True:
        try:
            length = int(input("Enter the desired password length: "))
        except ValueError:
            print("Invalid input! Please enter a numeric value for the length.")
            continue

        use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        use_lowercase = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
        use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
        use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'

        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
        
        if password:
            print(f"Generated password: {password}")

        another = input("Generate another password? (y/n): ").strip().lower()
        if another != 'y':
            print("Exiting the Password Generator.")
            break

if __name__ == "__main__":
    main()
