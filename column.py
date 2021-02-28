# Program to print out a column of consecutive numbers
# By Deon Fourie
# 6 March

n = int(input("Enter a number: "))
if -6 < n < 2:
    for x in range(n,n+41, 7):
        if n < 0:
            print(n)
        elif n < 10:
            print("", n)
        else:
            print(n)
        n += 7



















