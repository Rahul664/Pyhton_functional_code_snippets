

def dictmerge():
  #create two dictionaries as follows:

  dict1 = {'name':'Ramakrishna', 'age':25}
  dict2 = {'empid':1234, 'salary':5000}
  dict3 = {}
  #perform the following operations
  print("dict1, dict2: ", dict1, dict2)
  #create a single dict by merging the two dicts,
  dict3.update(dict1)
  dict3.update(dict2)
  print("dict3 is :", dict3)

  #update the salary to 10%
  print("dict3[salary]", dict3['salary'])
  dict3['salary'] = ( dict3['salary'] + ( (dict3['salary'] * 10) / 100) )
  print("after updating hte dict3 salary to 10 percent", dict3['salary'])

  #udpate the age to 26
  dict3['age'] = 26
  print("After updating the age to 26:", dict3)

  #insert a new element with key "grade" and assign value as "B1"
  dict3.update({'grade' :"B1"})
  print("inserting a new element:", dict3)

  #extract the keys and elements and print separetely
  print( "Printing keys of dictionary")
  print( dict3.keys())
  print ("Printing the values of dicitonary")
  print( dict3.values())
  
  #delete teh element with key 'age' and print the dict eleme
  print ("after deleting key=age and print dict3")
  del dict3['age']
  print (dict3)
  
