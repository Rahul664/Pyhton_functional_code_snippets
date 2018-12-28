counta=counte=counti=counto=countu=0
total_count=0
s=input("Enter the string to coount vowels")
a=s.split()
s1=""
for i in a:
    s1+=i
s1.lower()
for i in s1:
    if i=='a':
        counta+=1
        total_count+=1
    elif i=='e':
        counte+=1
        total_count+=1
    elif i=='i':
        counti+=1
        total_count+=1
    elif i=='o':
        counto+=1
        total_count+=1
    elif i=='u':
        countu+=1
        total_count+=1
print("Number of vowels",total_count)
if counta!=0:
    print("a",counta)
if counte!=0:
    print("e",counte)
if counti!=0:
    print("i",counti)
if counto!=0:
    print("o",counto)
if countu!=0:
    print("u",countu)
