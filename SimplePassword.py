
# Check if password meets basic requirements

# Ask for password input
password = input("Enter your password: ")

# Set minimum length requirement
min_length = 8

# Check password length
if len(password) >= min_length:
    print("Password is valid.")
else:
    print(f"Password is too short. It must be at least {min_length} characters long.")
