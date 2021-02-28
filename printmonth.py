# Program that prints a calendar
# By Deon Fourie
# 7 March

month = str(input("Enter the month ('January', ..., 'December'): "))
day = str(input("Enter the start day ('Monday', ..., 'Sunday'): "))

odd_months = ("January", "March", "May", "July", "August", "October", "December")
even_months = ("April", "June", "September", "November")
silly_month = "February"
days = ("Monday", "Tuesday", "Wednesday", 'Thursday', "Friday", "Saturday", "Sunday")
num = days.index(day)
calendar_days = "Mo Tu We Th Fr Sa Su"
if num == 0:
    i = 1
if num == 1:
    i = 0
if num == 2:
    i = -1
if num == 3:
    i = -2
if num == 4:
    i = -3
if num == 5:
    i = -4
if num == 6:
    i = -5
print(month)
print(calendar_days)
if month in odd_months:
    for x in range(6):
        for j in range(7):
            if i < 1:
                print("  ", end=" ")
            elif 1 <= i < 10:
                print("", i, end=" ")
            elif i <= 31:
                print(i, end=" ")
            else:
                print("  ", end=" ")
            i += 1
        print()

if month in even_months:
    for x in range(6):
        for j in range(7):
            if i < 1:
                print("  ", end=" ")
            elif 1 <= i < 10:
                print("", i, end=" ")
            elif i <= 30:
                print(i, end=" ")
            else:
                print("  ", end=" ")
            i += 1
        print()

if month == silly_month:
    for x in range(6):
        for j in range(7):
            if i < 1:
                print("  ", end=" ")
            elif 1 <= i < 10:
                print("", i, end=" ")
            elif i <= 28:
                print(i, end=" ")
            else:
                print("  ", end=" ")
            i += 1
        print()
