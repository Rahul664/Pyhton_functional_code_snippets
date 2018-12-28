def sortnum(num):
  for i in range(len(num)-1):
    for j in range(len(num)-1):
      if num[j] > num[j+1]:
        temp = num[j]
        num[j] = num[j+1]
        num[j+1] = temp
  print("sorted num: ", num)

def binarysearch(list1, item):
  list1.sort()
  first =0
  last = len(list1) - 1
  found = False

  while first<=last and not found:
    mid = int((first+last)/2)
    if list1[int(mid)] == item:
      found = True
      return found
    else:
      if item<list1[mid]:
        last = mid -1
      else:
        first = mid +1
  return found


def reverselist(list2):
  print(list2.reverse())
  print("reversed list: ", list2)