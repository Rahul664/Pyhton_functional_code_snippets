list1=[10,2,3,1,4,5]
list2=[1,2,3,4,5]
list3=[11,7,8,9,10,6,13]

print("length of list1","=",len(list1))
print("length of list2","=",len(list2))
print("length of list3","=",len(list3))
print(end="\n")
print("Max of list1","=",max(list1),"Min of list1","=",min(list1))
print("Max of list2","=",max(list2),"Min of list2","=",min(list2))
print("Max of list3","=",max(list3),"Min of list3","=",min(list3))
print(end="\n")
if list1>list2 and list1>list3:
    print("biggest list is list1")
elif list2>list1 and list2>list3:
    print("biggest list is list2")
elif list3>list1 and list3>list2:
    print("biggest list is list3")
print(end="\n")
if list1<list2 and list1<list3:
    print("smallest list is list1")
elif list2 < list1 and list2 < list3:
    print("smallest list is list2")
elif list3<list1 and list3<list2:
    print("smallest list is list3")
print(end="\n")
print("list after removing 1st and last elements")
list1.remove(list1[0])
list1.remove(list1[len(list1)-1])
print("list1",list1)

list2.remove(list2[0])
list2.remove(list2[len(list2)-1])
print("list2",list2)

list3.remove(list3[0])
list3.remove(list3[len(list3)-1])
print("list3",list3)
