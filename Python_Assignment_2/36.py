tup1 = (1,2,3,4)
tup2 = (56,65,54,43)
tup3=(251,25,5,11,5)
tup4=(251,25,5,11,5)
print(tup1,tup2)

print(end="\n")

print("tup1[0]", tup1[0])
print("tup1[:len(tup1)]" , tup1[:len(tup1)])
print("tup2[0:4]", tup2[0:4])

print(end="\n")


print("concatenation of tup1 and tup2 ",tup1+tup2)

print("id(tup1)",id(tup1))
print("id(tup2)",id(tup2))
print("id(tup1+tup2)",id(tup1+tup2))

print("deleting tup3")
del tup3

print("list(tup3)",list(tup4))
l1=list(tup4)
print("l1.remove(251) ",l1.remove(251))

print("tuple(l1)",tuple(l1))

print("length of tuple1: ", len(tup1))

print("(tup1) * 3 ", (tup1) * 3)
print("(2 in tup1)", (2 in tup1))



l = [1,2,3]
print("len(tup1) ", len(tup1))
print(" max(tup2)", max(tup2))
print("min(tup2) ", min(tup2))
tup6 = tuple(l)
print("list to tuple ", tup6)
print(type(tup6))
