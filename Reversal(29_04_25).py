n1 = int(input("Enter the number"))
rev = 0
while n1 > 0:
    d= n1 % 10
    rev = rev * 10 + d
    n1 //= 10
print(rev)
