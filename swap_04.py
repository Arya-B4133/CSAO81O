x = 10
y = 20
temp = x
x = y
y = temp
print("x:", x)
print("y:", y)

#without temporary

x = 10
y = 20
x, y = y, x
print("x:", x)
print("y:", y)
