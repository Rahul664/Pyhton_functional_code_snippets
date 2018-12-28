print("Reading 10 char from a file and print the pos till EOF")
f = open("rsh.txt", "r")
while 1:
    c=f.read(10)
    if ""==c:
        break
    print("Current cursor position",f.tell())
    print(c)

print("Resetting the file pointer after reading 100 character")
f.seek(0,0)
c = f.read(100)
print("Current position is",f.tell())
print(c)
f.seek(0,0)
print("After resetting Curr position is " ,f.tell())

print("Printing contents from 5th line onwards")
cnt=0
for l in f:
    cnt+=1
    if cnt>=5:
        print(l)
