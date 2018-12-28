import calendar
print("The calendar year 2016 ")
print (calendar.calendar(2016))

st = 1980
end = 2025
count=0
for i in range(1980,2025):
  if i%4 == 0:
    count+=1
print("Leap day in 1980 and 2025 are",count)

y = int(input("enter any year to check whether it is a loop year or not"))
if y%4 == 0:
  print("year %d is leap year"% y)
else:
  print("year %d is not a leap year" %y)

m = int(input("Enter any month of the year specified"))

print(calendar.month(2016,m))
