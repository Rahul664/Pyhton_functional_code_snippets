strlist=[]
f=open("rsh1.txt","r")
for l in f:
    a=l.split("\n")[0]
    strlist.append(a)
print("Printing form last line to first line")
for i in range(len(strlist)-1,-1,-1):
    print(strlist[i])
print("\n")
print("Printing reversed contents of easch line")
for i in range(len(strlist)):
    temp=strlist[i][::-1]
    print(temp)
