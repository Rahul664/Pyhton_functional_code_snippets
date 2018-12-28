key=0
num=[5,7,8,9,5,2,1,2,3,5,4]
print("Original array",num)
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[i]>num[j]:
            num[i],num[j]=num[j],num[i]
m=len(num)//2
h=len(num)
l=0
if key>=num[m]:
    l=m
    for i in range(l,h):
        if key==num[l]:
            print("Successful")
            break
        else:
            print("Unsuccessful")
            break
elif key<=num[m]:
    h=m
    for i in range(l,h):
        if key==num[l]:
            print("Successful")
            break
        else:
            print("Unsuccessful")
            break
