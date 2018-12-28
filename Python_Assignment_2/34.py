list1 = [1,1,2,3,4,5,5]
list2 = [12,12,23,34,45,56,56]
list3 = [67,67,78,89,90,98,98]
listmax = []
listmin=[]

list1.sort()
list2.sort()
list3.sort()

listmax.append(list1[len(list1)-1])
i=len(list1)-2
while list1[i]==listmax[len(listmax)-1]:
    i-=1
if i>=0:
    listmax.append(list1[i])

listmax.append(list2[len(list2)-1])
i=len(list2)-2
while list2[i]==listmax[len(listmax)-1]:
    i-=1
if i>=0:
    listmax.append(list2[i])

listmax.append(list3[len(list3)-1])
i=len(list3)-2
while list3[i]==listmax[len(listmax)-1]:
    i-=1
if i>=0:
    listmax.append(list3[i])

print("listmax",listmax)
print(end="\n")
avg=sum(listmax)/len(listmax)
print("Average of listmax %.2f" %avg)
print(end="\n")

listmin.append(list1[0])
i=1
while list1[i]==listmin[len(listmin)-1]:
    if i<=len(list1):
        i+=1
listmin.append(list1[i])

listmin.append(list2[0])
i=1
while list2[i]==listmin[len(listmin)-1]:
    if i<=len(list2):
        i+=1
listmin.append(list2[i])

listmin.append(list3[0])
i=1
while list3[i]==listmin[len(listmin)-1]:
    if i<=len(list3):
        i+=1
listmin.append(list3[i])

avg=sum(listmin)/len(listmin)
print("Average of listmin %.2f" %avg)
print(end="\n")
