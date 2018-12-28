
def file_oper():
  #read 10 characters from a file and print the position and do that till eof
  print ("read 10 char from a file an dprint hte pos and do till eof")
  from itertools import islice
  f = open("rsh1.txt", "r")
  while 1:
    char = f.read(10)
    if not char:  break
    print ("Current position is :%d "% (f.tell()))
    print (char)

  #reset the file pointer after reading 100 character from file use seek func
  print ("reset the file pointer after reading 100 character from file using seek func")
  f.seek(0,0)
  char = f.read(100)
  print ("Current position is :%d "% (f.tell()))
  print( char)
  f.seek(0,0)
  print( "After resetting to zero Curr position is :%d "% (f.tell()))
  print( "\n")

  #Open the file in read mode and start printing the contents from 5th line onwards
  print ("print the contents from 5th line onwards")
  char = f.readlines(5)
  print (char)
