# Function to check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Check a single number
num = int(input("Enter a number to check: "))
print(f"{num} is {check_even_odd(num)}")

# Check a list of numbers
number_list = [12, 7, 3, 18, 25, 42]

print("\nChecking a list of numbers:")
for n in number_list:
    print(f"{n} is {check_even_odd(n)}")
