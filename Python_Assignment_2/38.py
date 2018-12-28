dict1 = {'name':'RAHUL', 'age':22}
dict2 = {'empid':100, 'salary':23000}
dict3 = {}

print(dict1, dict2)
dict3.update(dict1)
dict3.update(dict2)
print(dict3)

dict3['salary'] = ( dict3['salary'] + ( (dict3['salary'] * 10) / 100) )
dict3['age'] = 26
print(dict3)

dict3.update({'grade' :"B1"})
print(dict3)

print("dict3 keys",dict3.keys())
print("dict3 values",dict3.values())

del dict3['age']
print("deleted key age")
print(dict3)
