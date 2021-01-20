# Exercise 47: Season from Month and Day

MONTHS = [None, "january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]

month, day = input("Please enter in a month (in full) and day: ").lower().split()
day = int(day)

month = MONTHS.index(month)

if month >= 12 and day >= 21:
    print("The season is Winter")
elif month >= 9 and day >= 22:
    print("The season is Fall")
elif month >= 6 and day >= 21:
    print("The season is Summer")
elif month >= 3 and day >= 20:
    print("The season is Spring")
else:
    print("The season is Winter")
