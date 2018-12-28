def fib(n):
  count =0
  n1 = 0
  n2 =1
  if n< 0:
    print("Not a positive integer")
  if n ==1:
    print(n1)
  else:
    while count < n:
      n3 = n1+n2
      print(n3)
      n1 = n2
      n2 = n3
      count +=1

fib(int(input("Enter the number n for fibonacci series")))
