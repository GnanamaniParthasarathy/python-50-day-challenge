
# Compare two numbers

# Get input from user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Compare the numbers
if num1 > num2:
    print(f"{num1} is greater than {num2}.")
elif num1 < num2:
    print(f"{num1} is less than {num2}.")
else:
    print(f"Both numbers are equal.")
