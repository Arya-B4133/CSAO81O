items = {"apple": 10, "banana": 5, "orange": 8}
cart = {}

while True:
    item = input("Enter item name (or 'done' to finish): ").lower()
    if item == 'done':
        break
    if item in items:
        quantity = int(input(f"Enter quantity for {item}: "))
        if item in cart:
            cart[item] += quantity
        else:
            cart[item] = quantity
    else:
        print("Item not found.")

total = sum(items[item] * quantity for item, quantity in cart.items())
print("Total price:", total)
