
# Take a full name and display it in different formats

# Get full name from user
full_name = input("Enter your full name (First Middle Last): ")

# Split the name into parts
name_parts = full_name.strip().split()

# Handle different name lengths
if len(name_parts) == 3:
    first, middle, last = name_parts
elif len(name_parts) == 2:
    first, last = name_parts
    middle = ""
else:
    print("Please enter at least a first and last name.")
    exit()

# Display in different formats
print(f"\n1. Last, First: {last}, {first}")
print(f"2. First Last: {first} {last}")
print(f"3. Initials: {first[0].upper()}.{middle[0].upper() + '.' if middle else ''}{last[0].upper()}.")
