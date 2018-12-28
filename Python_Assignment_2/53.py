print ("All 13 file functions mentioned  \n")

f = open("rsh1.txt", "r+")
print ("Name of the file is ", f.name)
f.close()

print ("--file.flush()--")
f = open("rsh1.txt","r+")
print ("Name of the file ", f.name)
f.flush()
f.close()


print ("--file.fileno()--")
f = open("rsh1.txt", "r+")
print ( "Name of the file ", f.name)
fid = f.fileno()
print ("File descriptor :", fid)
f.close()

print("--file.isatty()--")
f = open("rsh1.txt", "r+")
print ("Name of the file ", f.name)
ret = f.isatty()
print ("Return value: ",ret)
f.close()

print("--file.next()--")
f = open("rsh1.txt", "r+")
print("Name of the file ", f.name)
for index in range(2):
  line = next(f)
  print ("line no %d - %s" % (index, line))

f.close()

print("--file.read([size])--")
f = open("rsh1.txt", "r+")
print ("Name of the file ", f.name)
line = f.read(2)
print( "Read character: " ,line)
f.close()

print("--readlines()--")
f = open("rsh1.txt", "r+")
print ("Name of the file ", f.name)
line = f.readlines()
print ("Readlines :  %s" %(line))
line = f.readlines(4)
print ("Read lines : %s" %(line))
f.close()

print("--file.seek(offset[,whence])--")
f = open("rsh1.txt", "r+")
print ("Name of the file ", f.name)
line = f.readline()
print ("Readline :  %s" %(line))
print ("Set the pointer ot beginning")
f.seek(0,0)
line=f.readline(2)
print ("Readline() : %s " %(line))
f.close()


print("--file.tell()--")
f = open("rsh1.txt", "r+")
