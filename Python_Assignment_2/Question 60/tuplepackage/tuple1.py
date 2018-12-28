
def tuple_concat_operation():
  #a. create a tuple1 with days in a week and print
  tup1=('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
  print ("Print the tuple consist of days in a week: ", tup1)

  #b. create a tuple tup2 with months in a year and concatenate with tup1
  tup2 = ('january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',   'november', 'december')
  print ("printing the tuple of months of a year: ", tup2)

  tup3 = tup1+tup2
  print("tuple 3 is ", tup3)

  #c. Create 3 tuples wiht numbers and determine which is greater
  t1 = (1,2,3,4,5)
  t2 = (12,23,34,45,56)
  t3 = (67,78,89,90,98)
  t4 = ()
  print ("3 tuples are :", t1,t2,t3)
  
  if t1 > t2 and t1>t3:
    print( "tuple1 is greater: ", t1)
  if t2 > t3:
    print( "tuple2 is greater: ", t2)
  else:
    print ("tuple3 is greater: ", t3)


  #d. deleting tuple
 
  t4 = t1  + t2[2:]
  print("tuple 4 is :", t4)

  print( "deleting the tuple t4")
  del t4

  #inserting new element using list
  print("tuple1 :", t1)

  list1 = list(t1)
  elem = input("enter a number to be added")
  list1.append(elem)
  t1 = tuple(list1)
  print("inserting new elem, :", t1)
