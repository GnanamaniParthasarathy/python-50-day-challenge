
# Format a 10-digit number as (XXX) XXX-XXXX

def format_phone(number):
    number = ''.join(filter(str.isdigit, number))  # Keep only digits
    if len(number) == 10:
        return f"({number[:3]}) {number[3:6]}-{number[6:]}"
    else:
        return "Invalid number! Please enter exactly 10 digits."

# Example usage
phone = input("Enter a 10-digit phone number: ")
print("Formatted Number:", format_phone(phone))
