# Program that plots a function
# By Deon Fourie
# 2 April

import math

function = input("Enter a function f(x):\n")

for y in range (10, -11, -1):
    for x in range (-10, 11):
        f = round(eval(function))
        if x == 0 and y == 0 and y != f:
            print ("+", end="")
        elif y == 0 and y != f:
            print ("-", end="")
        elif x == 0 and y != f:
            print ("|", end="")
        elif y == f:
            print ("*", end="")
        else:
            print (" ", end="")
    print()