#a. Create 3 list wiht numbers and maxlist by taking max elem from each list

def list_manip():
  l1 = [1,2,3,4,5]
  l2 = [12,23,34,45,56]
  l3 = [67,78,89,90,98]
  lmax = []

  l1.sort()
  l2.sort()
  l3.sort()

  print("list are: ", l1,l2,l3)

  lmax.append(max(l1))
  lmax.append(max(l2))
  lmax.append(max(l3))
  lmax.append(l1[len(l1)-2])
  lmax.append(l2[len(l2)-2])
  lmax.append(l3[len(l3)-2])

  print("list wiht maximum elem in each list",lmax)

  #b. Find the average value from all elem of maxlist
  avg = float( sum(lmax)) / float(len(lmax))
  print("average value from the list",avg)

  #c.Create a list by taking two minimum elems from the list and  find average also
  lmin=[]
  lmin.append(min(l1))
  lmin.append(min(l2))
  lmin.append(min(l3))
  lmin.append(l1[1])
  lmin.append(l2[1])
  lmin.append(l3[1])
  print("minimum elem from list i s",lmin)

  avg1 = float(sum(lmin)) / float(len(lmin))
  print("average of minimum list is", avg1)
