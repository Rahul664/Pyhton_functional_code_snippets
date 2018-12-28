
#program for calculator using lambda function

def calculator(num1,num2):
  print ("enter the choice to do the operation ")
  print( "1.add\n 2.Sub\n 3.Mul\n 4.Div\n 5.Modulus\n 6.Floor Division\n")

  choice = int(input("enter your choice"))
  if choice == 1:
    add = lambda num1,num2 : num1+num2
    print( "additon:", add(num1,num2))
  elif choice == 2:
    sub = lambda num1,num2 : num1-num2
    print( "subtraction:", sub(num1,num2))
  elif choice == 3:
    mul = lambda num1,num2 : num1*num2
    print ("Multiplicaiton:", mul(num1,num2))
  elif choice == 4:
    if not num2 == 0:
      div = lambda num1,num2 : num1/num2
      print ("Division:", div(num1,num2))
    else:
      print( "infinity- cannot divide by zero")
  elif choice == 5:
    if not num2 == 0: 
      modulus = lambda num1,num2 : num1%num2
      print ("Modulus:", modulus(num1,num2))
    else:
      print ("infinity - cannot divide by zero" )
  elif choice == 6:
    if not num2 == 0:
      floor_div = lambda num1,num2 : num1//num2
      print ("floor division:", floor_div(num1,num2))
    else: 
      print ("infinity - cannot divide by zero")
  else:
    print ("Enter the input within the given choices")
    
