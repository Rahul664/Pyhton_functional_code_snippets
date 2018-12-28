

def vowel(name):
  count=0
  acount,ecount,icount,ocount,ucount=0,0,0,0,0
  for i in name:
    if i == 'a' or i == 'A':
      acount += 1 
      count +=1
      continue
    if i == 'e' or i == 'E':
      ecount += 1
      count +=1
      continue
    if i == 'i' or i == 'I':
      icount += 1
      count +=1
      continue
    if i == 'o' or i == 'O':
      ocount += 1  
      count +=1
      continue
    if i == 'u' or i == 'U':
      ucount += 1  
      count +=1
      continue
  print( "Total number of vowels in a string is %d" % count)
  print( "a = %d \n e = %d \n i = %d \n o = %d \n u = %d \n " % (acount, ecount, icount, ocount, ucount))
 
