import time
import calendar
localtime  = time.asctime(time.localtime(time.time()))

print("local current time is ", localtime)

cal = calendar.month(2018,9)
print(cal)
