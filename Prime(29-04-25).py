n=int(input("Enter a number:"))
p=True
if (n==0 or n==1):
    p=False
for i in range(2,n):
    if(n%i==0):
        p=False
    else:
        continue
if (p==True):
    print("The number is a prime number")
else:
    print("The number is not a prime number")
