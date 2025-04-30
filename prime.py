n=int(input("Enter the numeber:"))
p=True
for i in range(2,n,1):
    if n%i==0:
        p=False
    else:
        p=True
if p==True:
    print("Number is a prime number")
else:
    print("Number is not a prime number")
    
