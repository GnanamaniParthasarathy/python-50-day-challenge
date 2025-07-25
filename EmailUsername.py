
# Extract username from an email address

def extract_username(email):
    if "@" in email:
        return email.split("@")[0]
    else:
        return "Invalid email address"

# Example usage
email = input("Enter an email address: ")
print("Username:", extract_username(email))
