# Program that converts inches to metres
# By Deon Fourie
# 19 March

min1 = eval(input("Enter the minimum number of inches (not less than 0):\n"))
max1 = eval(input("Enter the maximum number of inches (not greater than 11):\n"))
min2 = min1
max2 = max1

if min1 >= 0:
    print("Inches: ", end="")
    for x in range(min1, max1+1):
        if min1 < 10:
            print("   ", min1, end=" ", sep="")
            min1 += 1
        else:
            print("  ", min1, end=" ", sep="")
            min1 += 1
print()
if max1 <= 11:
    print("Metres: ", end="")
    for y in range(min2, max2+1):
        num = min2 * 0.0254
        num = ('{:.2f}'.format(round(num, 2)))
        print(num, end=" ")
        min2 += 1



