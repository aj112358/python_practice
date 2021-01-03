# Exercise 25: Units of Time (Convert Seconds)

time = int(input("How many seconds to convert: "))

SECS_IN_MINS = 60
MINS_IN_HOURS = 60
HOURS_IN_DAYS = 24

SECS_IN_DAY = SECS_IN_MINS*MINS_IN_HOURS*HOURS_IN_DAYS
SECS_IN_HOUR = SECS_IN_MINS*MINS_IN_HOURS

days = time // SECS_IN_DAY
time = time % SECS_IN_DAY

hours = time // SECS_IN_HOUR
time = time % SECS_IN_HOUR

mins = time // SECS_IN_MINS
time = time % SECS_IN_MINS

seconds = time

print("%d:%02d:%02d:%02d" % (days, hours, mins, seconds))

#print(days)
#print(hours)
#print(mins)
#print(seconds)




