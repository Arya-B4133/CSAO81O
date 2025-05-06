import math

def calculate_gcd(a, b):
    return math.gcd(a, b)

def calculate_lcm(a, b):
    return abs(a * b) // math.gcd(a, b)
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

gcd = calculate_gcd(num1, num2)
lcm = calculate_lcm(num1, num2)

print(f"GCD of {num1} and {num2} is: {gcd}")
print(f"LCM of {num1} and {num2} is: {lcm}")
