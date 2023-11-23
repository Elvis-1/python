import sys

locations = sys.path
print(locations)
for i in locations:
    print(i)

import calendar # ensure you import your modules first
leapDays = calendar.leapdays(2000,2050)
print(leapDays)

isLeap = calendar.isleap(2030)
print(isLeap)