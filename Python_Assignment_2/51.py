import os
import sys

fil_array=[]
ldir=os.listdir(sys.argv[1])
file_count=0
for i in ldir:
    if i.endswith(".txt"):
        fil_array.append(os.path.join(sys.argv[1], i))
for i in fil_array:
    pattern_count=0
    f=open(i,"r")
    for l in f:
        if "Treasure" in l:
            pattern_count+=1
    if pattern_count>0:
        file_count+=1
    print("File name",os.path.basename(i),"Pattern count",pattern_count)
print("Total number of files with pattern is",file_count)
