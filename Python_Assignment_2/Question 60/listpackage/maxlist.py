

def max_list():
  #a. create 3 lists and find the lenght of each list and p rint
  l1=[1,2,3,4]
  l2=[12,23,34,45,22,333,33,22,1]
  l3=[54,43,32,78,68,3,33,333]
  print("3 lists are :", l1, "\n",l2,"\n", l3,"\n")
  len1 = len(l1)
  len2 = len(l2)
  len3 = len(l3)
  
  print("lenght of the three lists are: ", len1,len2,len3)

  #b. find max and min elem in each list
  print ("Maximum in list1: ", max(l1))
  print ("Maximum in list2: ", max(l2))
  print( "Maximum in list3: ", max(l3))

  #c. compare each list and determine which list is biggest and smallest
  if l1>l2 and l1>l3:
    print("List1 is bigger:" , l1)
  elif l2>l3:
    print("List2 is bigger:" , l2)
  else:
    print("List3 is bigger:" , l3)

  #d. Delete first and last element of list and print contents
  l1.pop(0)
  l1.pop(len(l1)-1)
  print("Deleting hte first and last element of the list and printing the contents list1: ", l1)

  l2.pop(0)
  l2.pop(len(l2)-1)
  print("list2 :", l2)

  l3.pop(0)
  l3.pop(len(l3)-1)
  print("list3 :", l3)

