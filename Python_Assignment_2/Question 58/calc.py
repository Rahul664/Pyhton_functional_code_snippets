import math

def add(a,b):
  'this adds 2 num'
  print("sum of a and b", a+b)

def diff(a,b):
  'diff btn 2 num'
  print("diff of 2 num", a-b)

def mul(a,b):
  'multiples a with b'
  print("Mul of a and b", a*b)

def div(a,b):
  'divides 2 nos'
  if b==0:
    print("enter a nonzero num")
  else:
    print("div a/b is ", a/b)

def sqroot(a):
  print("square root of number", a , "is ", math.sqrt(a))

def floor_div(a,b):
  print("floor division of a and b is ", a//b)

def fib(nterms):
  a=0
  b=1
  if nterms<0:
    print("please enter positive num")
  elif nterms ==1:
    print("fibo... ", a)
  elif nterms ==2:
    print (a)
    print( b)
  else:
    print( a)
    print( b)
    while(nterms>2):
      next=a+b
      print(next)
      a=b
      b=next
      nterms=nterms-1


def isprime(num):
  if num>1:
    for i in range(2,num):
      if(num %i) == 0:
        print(num, "not a prime num")
        break
    else:
      print(num, " is a  prime")