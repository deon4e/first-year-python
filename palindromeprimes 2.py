# Recurive version of previous palindrome question
# By Deon Fourie
# 25 April

import sys
sys.setrecursionlimit(30000)

def reverse(phrase):
    """This function reverses a phrase"""
    if phrase == "":
        return phrase
    else:
        return reverse(phrase[1:]) + phrase[0]

def primenumber(value, last=1):
    """This function produces prime numbers"""
    if last == value:
        return True
    else:
        if value % last == 0 and last != 1:
            return False
        else:
            return primenumber(value, last + 1)

def printlist1(array1, pos=0):
    """This function simply prints an array"""
    if pos < len(array1):
        print(array1[pos])
        return printlist1(array1, pos + 1)

def palindromeprimes(num1, num2, list1):
    """This function finds primes that are palindromic"""
    if num1 >= num2:
        if primenumber(num1, 1):
            if num1 == int(reverse(str(num1))):
                list1.append(num1)
        palindromeprimes(num1 - 1, num2, list1)

def main():
    list1 = []
    num2 = eval(input("Enter the starting point N: \n"))
    num1 = eval(input("Enter the ending point M: \n"))
    print("The palindromic primes are:")
    palindromeprimes(num1, num2, list1)
    array1 = sorted(list1)
    return printlist1(array1, 0)

main()