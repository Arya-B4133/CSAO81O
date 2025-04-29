n=int(input("Enter a number:"))
sum=0
l=len(str(n))
int(l)
while (n>0):
    rem=n%10
    sum=sum+rem
    n=n//10
print("Sum of the digits of the number is:", sum)
