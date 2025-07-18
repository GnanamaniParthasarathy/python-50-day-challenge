
# Calculate total cost of 3 items including tax

# Get prices of the items
item1 = float(input("Enter price of item 1: "))
item2 = float(input("Enter price of item 2: "))
item3 = float(input("Enter price of item 3: "))

# Get tax percentage
tax_percent = float(input("Enter tax percentage: "))

# Calculate subtotal
subtotal = item1 + item2 + item3

# Calculate tax amount
tax_amount = (tax_percent / 100) * subtotal

# Calculate total cost
total_cost = subtotal + tax_amount

# Display results
print(f"\nSubtotal: ₹{subtotal:.2f}")
print(f"Tax: ₹{tax_amount:.2f}")
print(f"Total cost including tax: ₹{total_cost:.2f}")
