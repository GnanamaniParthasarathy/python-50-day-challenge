
# Count positive, negative, and zero numbers in a list

# Sample list
numbers = [5, -3, 0, 12, -7, 0, 9, -1, 0]

# Initialize counters
positive_count = 0
negative_count = 0
zero_count = 0

# Loop through the list and count
for num in numbers:
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    else:
        zero_count += 1

# Display the result
print(f"Positive numbers: {positive_count}")
print(f"Negative numbers: {negative_count}")
print(f"Zeros: {zero_count}")
