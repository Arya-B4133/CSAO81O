n=int(input("Enter the number:"))
sum=0
for i in range(1,n,1):
    if n%i==0:
        sum=sum+i
if(sum==n):
    print("Number is a perfect number.")
else:
    print("Number is not a perfect number.")
