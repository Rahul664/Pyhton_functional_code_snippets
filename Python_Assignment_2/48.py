import math

print("Python Calculator")
num1 = float(input("Enter the first number"))
num2 = float(input("Enter the second number"))

print("Enter the ch to do the operation ")
print("1.add\n 2.Sub\n 3.Mul\n 4.Div\n")


def add(num1, num2):
    return num1 + num2
def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


def sqrt(num):
    return math.sqrt(num)


def substr(string, delim):
    sub = string.split(delim)
    return sub


ch = int(input("Enter your choice of operation"))
if ch == 1:
    num3 = add(num1, num2)
    print("Addition of %f + %f is %f" % (num1, num2, num3), "\n")
elif ch == 2:
    num3 = sub(num1, num2)
    print("Subtraction of %f - %f is %f" % (num1, num2, num3), "\n")
elif ch == 3:
    num3 = mul(num1, num2)
    print("Multiplication of %f * %f is %f" % (num1, num2, num3), "\n")
elif ch == 4:
    if not num2 == 0:
        num3 = div(num1, num2)
        print("Division of %f / %f is %f" % (num1, num2, num3), "\n")
    else:
        print("Division by zero error\n")
else:
    print("Enter the input within the given chs  \n")

print("Finding the sqroot of number")
sqnum = float(input("enter a number"))
print("square root is:", sqrt(sqnum), "\n")

print("Substring from the given string using delimiter")
string = input("Enter a string")
delim = input("enter the delimiter to create a substring")
substring = substr(string, delim)
print("Substring is :", substring)
