import math

try:
    r=int(input("Enter the radius of circle"))
except ValueError:
    print("Enter Numeric values only")

if r<=0:
    print("Radius cannot be negative")
    exit(0)
else:
    print("The area of circle is","=",math.pi*r**2)
