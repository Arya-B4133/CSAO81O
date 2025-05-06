import math

def factorial(n):
    return math.factorial(n)

def find_largest(numbers):
    return max(numbers)

def calculate_area(shape):
    shape = shape.lower()
    if shape == "rectangle":
        length = float(input("Enter length: "))
        breadth = float(input("Enter breadth: "))
        return length * breadth
    elif shape == "square":
        side = float(input("Enter side length: "))
        return side ** 2
    elif shape == "circle":
        radius = float(input("Enter radius: "))
        return math.pi * radius ** 2
    else:
        return "Shape not recognized"

num = int(input("Enter a number for factorial: "))
print(f"Factorial of {num}: {factorial(num)}")

numbers = list(map(int, input("Enter numbers separated by space to find the largest: ").split()))
print(f"Largest number: {find_largest(numbers)}")

shape = input("Enter the shape (rectangle, square, circle) to calculate area: ")
print(f"Area: {calculate_area(shape)}")
