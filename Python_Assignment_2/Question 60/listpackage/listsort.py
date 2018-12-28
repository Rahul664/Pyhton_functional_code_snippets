

def list_sort():
  #a. create a list o f7 elements and append an obj 80 to the list
  l1 = [10,20,30,40,50,60,70]
  print ("Original list: ", l1)
  l1.append(80)
  print("after appending 80 to the list: ", l1)


  #b. insert 100 at 4th position
  l1.insert(3,100)
  print ("After inserting 100 in 4th position: ", l1)

  #c. sort and pirnt all elem
  l1.sort()
  print("After sorting : ", l1)

  l2 = sorted(l1,key = int, reverse = True)
  print("printing the sorted elem list2: ", l2)

  #c. delete last  3 elem
  l2.pop(len(l2)-1)
  l2.pop(len(l2)-1)
  l2.pop(len(l2)-1)
  print("deleting last 3 elems", l2)
