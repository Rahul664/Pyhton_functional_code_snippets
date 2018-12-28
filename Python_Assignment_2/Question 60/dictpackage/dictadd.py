
#perform teh following operations in dictionary
#create 3 dict with 3 elem each
def dictoper():
  dict1 = {"empname":"john", "empid":123, "location":"chennai" }
  dict2 = {"empname":"Sam", "empid":345, "location":"Hyderabad" }
  dict3 = {"empname":"Mavel", "empid":567, "location":"Kolkata" }
  print( dict1,"\t",dict2,"\t", dict3)


  #add new elem in dict1 and dict2
  dict1.update({"designation":"sr.engr"})
  print( dict1)
  dict2.update({"designation":"sr.manager"})
  print (dict2)

  #print the lenght of dict1, dict2 , dict3
  print ("length of dict1",len(dict1))
  print ("length of dict1",len(dict2))
  print ("length of dict1",len(dict3))

  #convert all the dict to string and concatenate them
  str1=str(dict1)
  print ("type of str1", type(str1))
  print("str1 is ", str1)
  str2=str(dict2)
  str3=str(dict3)
  str4 = str1+str2+str3
  print ("converting dict to string:", str4)
