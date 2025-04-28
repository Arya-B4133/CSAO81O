a=int(input('Enter the First number:'))
b=int(input('Enter the Second number:'))
c=int(input('Enter the Third number:'))
quad=(b**2-4*a*c)
if (quad==0):
    print("Same and real roots")
elif(quad>0):
    print("Different real roots")
else:
    print("Imaginary roots")
