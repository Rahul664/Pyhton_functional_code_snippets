import math
import sys

try:
  num = a/2
  print ("num is ", num)
except Exception:
  print("Exception - base class for all exception")

#Arithmetic errror
try:
  div = 2/0
except ArithmeticError:
  print( "Arithmetic error exception")

#StopIteration
try:
  #z=[1,2]
  f1=open("rsh1.txt")
  for i in range(1,4):
    print( next(f1))
except StopIteration:
  print("Stop Iteration Exception")
f1.close()


#SystemExit
try:
  sys.exit()
except SystemExit:
  print("System exit exception")

#Overflow error
try:
  a=math.exp(3456/3456789*2345670987)
  print("a is ",a)
except OverflowError:
  print("Overflow error exception")

#Value Error
try:
  a=math.sqrt(-44/5)
  print("a is ",a)
except ValueError:
  print("Value error")

#Zero division error
try:
  num = 56789/0
  print("num is ", num)
except ZeroDivisionError:
  print("ZeroDivisionError - cannot divide by zero")

#assertion error
try:
  val = 9
  assert(val<9), "Value should be less than 9"
except AssertionError as err:
  print(err)

#Attribute error
try:
  i = 9
  i.append(4)
except AttributeError:
  print("AttributeError - integer has not attribute append")


#EOF error
try:
  f2=open("rsh1.txt","r")
  f2.read()
except EOFError:
  print("EOF error")

#import error
try:
  import sample
except ImportError:
  print("import error exception")

#look up error
dict={'empid':'empname'}
try:
  print (dict['name'])
except LookupError:
  print('lookup error')

#index error
try:
  l1=[1,2,3,4]
  print("list l1 is ", l1)
  print("list l1[9]", l1[9])
except IndexError:
  print("IndexoutofBound")

#name error:
try:
  print( name_n)
except NameError:
  print("name error")

#keyboard interrupt
try:
  name = input("Enter your name:")
  print("you entered: " + name)
except KeyboardInterrupt:
  print( "Keyboard interrupt you hit ctrl-c")

#Key error
try:
  print("dict is ", dict['2'])
except:
  print("key error")

#unbound local error
counter=0
def incre():
  try:
    counter+=1
  except UnboundLocalError:
    print("Unbound local error")

incre()

#IOError
try:
  f4=open('rsh1.txt',"r")
  f4.write("Write at the end")
except IOError:
  print("Writnig in a file opened in read mode, IOError")

#notimplemented error
try:
  class shape(object):
    @property
    def rect(self):
      raise NotImplementedError("Notimplemented error - subclass should implement this method")

  s=shape()
  print(s.rect)
except Exception as e:
  print(e)

#runtime error
try:
  raise RuntimeError
except RuntimeError:
  print("runtime error occured")

#typeerror
try:
  stri="hello"
  stri = stri-1
except TypeError:
  print("Type error")

#value error:
try:
  stri= "hey"
  print(int(stri))
except ValueError:
  print("value error")
