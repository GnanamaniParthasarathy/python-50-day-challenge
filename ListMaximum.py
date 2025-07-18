
# Find the largest number in a list without using max()

# Sample list
numbers = [23, 87, 45, 12, 99, 34, 65]

# Assume the first number is the largest
largest = numbers[0]

# Loop through the list to find the largest
for num in numbers:
    if num > largest:
        largest = num

# Display the result
print(f"The largest number in the list is: {largest}")
