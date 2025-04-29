a=int(input("Enter a variable:"))
b=int(input("Enter a variable:"))
c=int(input("Enter a variable:"))
if(a>b):
    if(a>c):
        print(a,"is the greatest of number")
    else:
        print(c,"is the greatest number")
elif (b>c):
    print(b,"is the greatest number")
