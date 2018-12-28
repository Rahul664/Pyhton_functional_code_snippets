list1 = [10,20,30,40,50,60,70]
print("Original list", list1)
list1.append(80)
print("Appending 80 to the list: ", list1)

list1.insert(3,100)
print("After inserting 100 in 4th position: ", list1)

list1.sort()
print("After sorting : ", list1)

list2 = sorted(list1,key = int, reverse = True)
print(list2)

list2.pop(len(list2)-1)
list2.pop(len(list2)-1)
list2.pop(len(list2)-1)
print(list2)
