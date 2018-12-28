num1 = float(input("Enter the 1st number"))
num2 = float(input("Enter the 2nd number"))

print("Enter the choice of  operation to perform ")
print("1.add\t 2.Sub\t 3.Mul\t 4.Div\t 5.Modulus\t 6.Floor Division\t 7.Exit\n")

while(1):
  ip = int(input("enter your choice"))
  if ip == 1:
    add = lambda num1,num2 : num1+num2
    print("Sum:", add(num1,num2))
  elif ip == 2:
    sub = lambda num1,num2 : num1-num2
    print("Subtraction is:", sub(num1,num2))
  elif ip == 3:
    mul = lambda num1,num2 : num1*num2
    print("Product is :", mul(num1,num2))
  elif ip == 4:
    if not num2 == 0:
      div = lambda num1,num2 : num1/num2
      print("Division is:", div(num1,num2))
    else:
      print("Division by zero is not possible")
  elif ip == 5:
    if not num2 == 0:
      modulus = lambda num1,num2 : num1%num2
      print("Modulus:", modulus(num1,num2))
    else:
      print("Division by zero is not possible")
  elif ip == 6:
    if not num2 == 0:
      floor_div = lambda num1,num2 : num1//num2
      print("Result of floor division:", floor_div(num1,num2))
    else:
      print("Division by zero is not possible")
  elif ip == 7:
    break
  else:
    print("Enter the choice of  operation to perform ")
    break
