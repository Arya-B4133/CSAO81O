def arithmetic_series(start, difference, terms):
    series = [start + i * difference for i in range(terms)]
    return series

start = int(input("Enter the starting number: "))
difference = int(input("Enter the common difference: "))
terms = int(input("Enter the number of terms: "))
print("Arithmetic Series:", arithmetic_series(start, difference, terms))
def full_pyramid_numbers(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")
        print(" ".join(str(x) for x in range(1, 2 * i)))
        
rows = int(input("Enter the number of rows: "))
full_pyramid_numbers(rows)
