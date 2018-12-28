import time
try:
  name = input("Enter your name:")
  print("you entered: " + name)
except KeyboardInterrupt:
  print( "Keyboard interrupt you hit ctrl-c")

i=1
try:
  while(i<5):
    time.sleep(1)
    print (i)
    i += 1
except KeyboardInterrupt:
  print( "Keyboard interrupt")


try:
  print ("Hi" +" "+ n)
except NameError:
  print ("variable n is not defined or name error")

#arithmetic error
try:
  a=89/0
except ArithmeticError:
  print ("Division by zero error")
