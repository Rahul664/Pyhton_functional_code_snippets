
#search func from the list
#function should receive variable lenght arguments present in the list

def search(*argv):
  list1 = [1,2,3,34,45,56,67,768,788,76,75]
  for arg in argv:
    for i in list1:
      if arg == i:
        print ("The given element %f is there in the list" % arg)
        break
    else:
      print( "The given element %f is not there in the list" % arg)
   


