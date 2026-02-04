import string

# Load common passwords from a file
def load_common_passwords(filepath='common_passwords.txt'):
    try:
        with open(filepath, 'r') as file:
            return set(line.strip() for line in file)
    except FileNotFoundError:
        print("⚠️ Warning: 'common_passwords.txt' not found. Skipping common password check.")
        return set()

# Check password strength and return rating and suggestions
def check_strength(password, common_passwords):
    score = 0
    feedback = []

    # Length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Upper and lower case
    if any(c.islower() for c in password) and any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Use both uppercase and lowercase letters.")

    # Numbers
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Include at least one number.")

    # Special characters
    if any(c in string.punctuation for c in password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$, etc).")

    # Common password check
    if password.lower() in common_passwords:
        feedback.append("This password is too common.")
    else:
        score += 1

    # Rating based on score
    if score <= 2:
        rating = "Weak"
    elif score == 3 or score == 4:
        rating = "Moderate"
    else:
        rating = "Strong"

    return rating, feedback

# Main program loop
def main():
    common_passwords = load_common_passwords()

    print(" Password Strength Checker")
    print("Type 'exit' to quit.\n")

    while True:
        password = input("Enter a password to check: ")

        if password.lower() == 'exit':
            print("Goodbye! 👋")
            break

        rating, feedback = check_strength(password, common_passwords)
        print(f"\nPassword Strength: {rating}")

        if feedback:
            print("Suggestions:")
            for f in feedback:
                print(f" - {f}")
        print()  # spacing

if __name__ == "__main__":
    main()
