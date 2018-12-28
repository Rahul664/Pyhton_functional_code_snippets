import random
import math

test_array=[10,20,50,40,30]
print("Enter number to round to next decimal point")
print("The round of the number is",round(float(input())))
print("Enter number to find the square root")
print("The square root of the number is",math.sqrt(float(input())))
print("Random number between 1 and 10 using random() function is",random.randint(1,10))
print("Random number between 10 and 500 using uniform() function is",random.uniform(10,500))

'''Math and Random module functions'''
print("Some Math and Random modules functions")

print("Example of math.ceil(2.3)",math.ceil(2.3))
print("Example of math.floor(2.5)",math.floor(2.5))
print("math.factorial(5)",math.factorial(5))
print("math.copysign(5,-4)",math.copysign(5,-4))
print("random.random()",random.random())
print("random.sample(range(100),10)",random.sample(range(100),10))
print("random.choice(range(10))",random.choice(test_array))
print("math.pow(5,2)",math.pow(5,2))
