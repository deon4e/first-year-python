# Program that prints a table of feet and inches to metres
# By Deon Fourie
# 19 March
from math import ceil


start = eval(input("Enter the minimum number of feet (not less than 0):\n"))
ending = eval(input("Enter the maximum number of feet (not more than 30):\n"))
print()
print("""      |   0"   1"   2"   3"   4"   5"   6"   7"   8"   9"  10"  11" """)
feet = start
count = 0
if start >= 0 and ending <= 30:
    for x in range(feet, ending+1):
        if feet < 10:
                print("   ", feet, "'", " | ", sep="", end="")
                feet += 1
                for y in range(12):
                    num = start * 0.3048
                    num = num + count * 0.0254
                    num = ('{:.2f}'.format(round(num, 2)))
                    print(num, end=" ")
                    count += 1
                print()
        else:
            print("  ", feet, "' | ", sep="", end="")
            feet += 1
            for y in range(12):
                num = start * 0.3048
                num = num + count * 0.0254
                num = ('{:.2f}'.format(round(num, 2)))
                print(num, end=" ")
                count += 1
            print()
