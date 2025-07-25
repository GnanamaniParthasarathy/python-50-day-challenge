
import math

# Function to calculate area of a circle
def area_circle(radius):
    return math.pi * radius ** 2

# Function to calculate area of a rectangle
def area_rectangle(length, width):
    return length * width

# Function to calculate area of a triangle
def area_triangle(base, height):
    return 0.5 * base * height

# Example usage
print("Choose a shape to calculate area:")
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")

choice = input("Enter choice (1/2/3): ")

if choice == '1':
    r = float(input("Enter radius: "))
    print("Area of Circle:", area_circle(r))
elif choice == '2':
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    print("Area of Rectangle:", area_rectangle(l, w))
elif choice == '3':
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    print("Area of Triangle:", area_triangle(b, h))
else:
    print("Invalid choice")
