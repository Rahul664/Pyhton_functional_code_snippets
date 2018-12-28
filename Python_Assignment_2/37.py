dict1 = {"ename":"Rohini", "eid":123, "loc":"Bangalore" }
dict2 = {"ename":"Rahul", "eid":456, "loc":"Mumbai" }
dict3 = {"ename":"Jim", "eid":789, "loc":"Chennai" }

print(dict1,"\t",dict2,"\t", dict3)

dict1.update({"job_title":"sr.engr"})
print(dict1)
dict2.update({"job_title":"sr.manager"})
print(dict2)

print("len(dict1)",len(dict1))
print("len(dict1)",len(dict2))
print("len(dict1)",len(dict3))


s1=str(dict1)
print(type(s1))
print(s1)
s2=str(dict2)
s3=str(dict3)
s4 = s1+s2+s3
print(s4)
