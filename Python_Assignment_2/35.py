tup1=('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
print ("tuple consist of days in a week: ", tup1)

tup2 = ('january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december')
print ("tuple of months of a year: ", tup2)

tup3 = tup1+tup2
print("Concatenated tuple",tup3)

tup1 = (1,2,3,4,5)
tup2 = (12,23,34,45,56)
tup3 = (67,78,89,90,98)

print(tup1,tup2,tup3)

if tup1 > tup2 and tup1>tup3:
  print("tuple1 is greater: ", tup1)
elif tup2 > tup3 and tup1>tup2:
  print("tuple2 is greater: ", tup2)
elif tup3>tup2 and tup3>tup1:
  print("tuple3 is greater: ", tup3)

tup4 = tup1
print("tuple4 before deleting individual element",tup4)
tup4=tup4[1:]
print("tuple4 after deleting 1st element",tup4)

print("Deleting the tuple tup4")
del tup4

tup4=()
list1=list(tup4)
for i in range(4):
    list1.append(i)
tup4=tuple(list1)
print("Inserted to tuple after typecasting to list",tup4)
