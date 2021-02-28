# Program that convert feet to metres
# By Deon Fourie
# 19 March

start = eval(input("Enter the minimum number of feet (not less than 0):\n"))
ending = eval(input("Enter the maximum number of feet (not more than 99):\n"))
if start >= 0 and ending <= 99:
    for x in range(start, ending+1):
        if start < 10:
            num1 = start * 0.3048
            num1 = ('{:.2f}'.format(round(num1, 2)))
            print("   ", start, "'", " |   ", num1, "m", sep="")
            start += 1
        else:
            num2 = start * 0.3048
            num2 = ('{:.2f}'.format(round(num2, 2)))
            print("  ", start, "'", " |   ", num2, "m", sep="")
            start += 1
