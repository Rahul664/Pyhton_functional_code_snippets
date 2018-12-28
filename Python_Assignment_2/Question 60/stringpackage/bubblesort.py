
def bubblesort(l1):
  n = len(l1)
  for a in range(n):
    for b in range(0,n-a-1):
      if l1[b]>l1[b+1]:
        l1[b],l1[b+1]=l1[b+1],l1[b]
  
  print ("The sorted list is :", l1)
 
