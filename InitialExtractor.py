
# Extract initials from full name

def get_initials(full_name):
    # Remove leading/trailing spaces and split by space
    words = full_name.strip().split()
    # Take the first letter of each word, make it uppercase
    initials = ''.join([word[0].upper() for word in words if word])
    return initials

# Example usage
name = input("Enter full name: ")
print("Initials:", get_initials(name))
