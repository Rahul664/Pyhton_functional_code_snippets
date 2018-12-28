from datetime import *
import time
import cProfile
import re

print("Printing the current time for every 5 seconds upto one minute ",end="\n")
res = datetime.now() + timedelta(seconds = 60)
print(res, end="\n")

while(datetime.now() < res):
  print(time.asctime(time.localtime(time.time())))
  time.sleep(5)


cProfile.run('re.compile("32.py")')
