try:
  f = open("rsh1.txt", "r")
  print(f.read())
  f.write("Hello")
except IOError:
  print("File is opened in read mode")

print("\n")
try:
  num = int(input("Enter value:"))
  print("Printing the entered value", num)
except ValueError:
  print("Value Error")
