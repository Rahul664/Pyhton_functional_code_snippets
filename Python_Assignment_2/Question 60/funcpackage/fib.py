
#using fib(n) func-generate fibonacci
# n-userspecified argument where number of elements in series


def fib(n):
  count =0
  n1 = 0
  n2 =1
  if n< 0:
    print( "Enter positive numbers")
  if n ==1:
    print( n1)
  else:
    while count < n:
      n3 = n1+n2
      print( n3)
      n1 = n2
      n2 = n3
      count +=1 


