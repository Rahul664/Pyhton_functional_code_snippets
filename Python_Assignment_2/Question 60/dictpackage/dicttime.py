

def dicttime():
  #print current date and time and 
  import time
  import calendar
  localtime  = time.asctime(time.localtime(time.time()))
  print ("local current time is ", localtime)

  #print current month calender
  cal = calendar.month(2018,7)
  print( cal)
