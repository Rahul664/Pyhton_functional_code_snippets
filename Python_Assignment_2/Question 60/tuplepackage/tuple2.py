
def tuple_operations():
  #create two tuples
  tup1 = (1,2,3,4,"abcd","defg")
  tup2 = (23,34,45,56,65,54,43)

  print("Tuple1 and tuple2 are:",  tup1,tup2)

  print( "\n")
  #access the elements
  print ("tuple elements", tup1[0])
  print( "tuple elems" , tup1[:len(tup1)])
  print( "slicing", tup2[0:4])

  print( "\n")
  #updating tuples
  print ("tuples are immutable so there is no updating the tuple")
  print( "concatenation is possible-will create a new tuple")
  tup3 = tup1+tup2
  print("tuple3 is :",tup3)
  print( id(tup1),"address of tuple1")
  print (id(tup2), "address of tuple2")
  print( id(tup1+tup2), "shows that the address is different")
  print( id(tup3))

  #to remove tuple
  print ("\n")
  print ("removing tuple")
  print ("convert the tuple to list and do the deletion operation")
  print ("tuple 3", tup3)
  l1 = list(tup3)
  print ("converted to list: ",l1)
  l1.remove(1)
  print ("list after removing 1: ",l1)
  tup3 = tuple(l1)
  print ("converte to tuple: ",tup3)
  

  #basic tuple operations:
  print( "length of tuple1: ", len(tup1))
  print( "concatenating two tuples:", tup1+tup2)
  print ("repetition: ", (tup1) * 3)
  print ("membership -check for elem in tuple: ", (2 in tup1))
  print ("iteraiton :" )
  for i in tup1:  
    print( i)
  

  print ("\n")
  #basic functions
  lis = [1,2,3]

  print ("length of tuple: ", len(tup1))
  print (" max of tuple: ", max(tup2))
  print( "min of tuple: ", min(tup2))
  tup7 = tuple(lis)
  print ("converitng list ot tuple: ", tup7)
  print("type(tup7)", type(tup7))
