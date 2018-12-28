num=[5,7,8,9,5,2,1,2,3,5,4]
print("Original array",num)
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[i]>num[j]:
            num[i],num[j]=num[j],num[i]
print("Sorted array",num)
