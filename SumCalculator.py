
# Find the sum of numbers from 1 to n

# Get input from the user
n = int(input("Enter a positive integer (n): "))

# Initialize sum
total = 0

# Loop from 1 to n
for i in range(1, n + 1):
    total += i

# Display the result
print(f"The sum of numbers from 1 to {n} is: {total}")
