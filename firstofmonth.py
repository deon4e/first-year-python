# Program to calculate the first day of a given month in a given year
# By Deon Fourie
# 19 March

month = str(input("Enter the month: "))
year = eval(input("Enter the year: "))
month_cpy = month
# if year is a leap year
if year % 400 == 0:
    if month == "January":
        month = 0
    elif month == "February":
        month = 3
    elif month == "March":
        month = 4
    elif month == "April":
        month = 0
    elif month == "May":
        month = 2
    elif month == "June":
        month = 5
    elif month == "July":
        month = 0
    elif month == "August":
        month = 3
    elif month == "September":
        month = 6
    elif month == "October":
        month = 1
    elif month == "November":
        month = 4
    elif month == "December":
        month = 6
    x = year - 1
    day = 1
    day = day + month
    day = day + (5 * (x % 4))
    day = day + (4 * (x % 100))
    day = day + (6 * (x % 400))
    day = day % 7

elif year % 400 != 0 and year % 100 != 0 and year % 4 == 0:
    if month == "January":
        month = 0
    elif month == "February":
        month = 3
    elif month == "March":
        month = 4
    elif month == "April":
        month = 0
    elif month == "May":
        month = 2
    elif month == "June":
        month = 5
    elif month == "July":
        month = 0
    elif month == "August":
        month = 3
    elif month == "September":
        month = 6
    elif month == "October":
        month = 1
    elif month == "November":
        month = 4
    elif month == "December":
        month = 6
    x = year - 1
    day = 1
    day = day + month
    day = day + (5 * (x % 4))
    day = day + (4 * (x % 100))
    day = day + (6 * (x % 400))
    day = day % 7

else: # if year is a common year
    if month == "January":
        month = 0
    elif month == "February":
        month = 3
    elif month == "March":
        month = 3
    elif month == "April":
        month = 6
    elif month == "May":
        month = 1
    elif month == "June":
        month = 4
    elif month == "July":
        month = 6
    elif month == "August":
        month = 2
    elif month == "September":
        month = 5
    elif month == "October":
        month = 0
    elif month == "November":
        month = 3
    elif month == "December":
        month = 5
    x = year - 1
    day = 1
    day = day + month
    day = day + (5 * (x % 4))
    day = day + (4 * (x % 100))
    day = day + (6 * (x % 400))
    day = day % 7

if day == 0:
            day = 'Sunday.'
if day == 1:
            day = 'Monday.'
if day == 2:
            day = 'Tuesday.'
if day == 3:
            day = 'Wednesday.'
if day == 4:
            day = 'Thursday.'
if day == 5:
            day = 'Friday.'
if day == 6:
            day = 'Saturday.'
if day == 7:
            day = 'Sunday.'

print("The 1st of", month_cpy,  year, "is a", day)
