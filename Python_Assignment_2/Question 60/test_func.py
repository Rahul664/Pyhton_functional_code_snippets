from funcpackage import calc
from funcpackage import fib
from funcpackage import search

n = int(input("enter the number of elements for printing the fibonacci series"))
fib.fib(n)

print("enter the twonumbers for calculator functionality")
num1 = float(input("enter the fir st number"))
num2 = float(input("enter the second number"))
calc.calculator(num1,num2)

print("searching the following numbers, 890, 1,2....")
search.search(890)
search.search(1,2)
search.search(-23)
search.search(00)
search.search(3.233)
search.search(2,3,7777)
