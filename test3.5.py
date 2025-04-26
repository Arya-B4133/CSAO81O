ch=int(input("What would you like to check\n[1]SQUARE?\n[2]CIRCLE?\n=>"))
if (ch==1):
    a=int(input("ENTER THE SIDE LENGTH"))
    sarea=a**2
    print("The area of a square is", sarea)
else:
    r=int(input("Enter the radius:"))
    area=r*r*3.14
    print("Area of a circle is", area)
