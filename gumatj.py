# Gumatj calculator
# By Deon Fourie
# 24 March

def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]

def decimal_to_gumatj(a):
    num1 = ""
    num2 = ""
    if a == 0:
        return 0
    while a != 0:
        num1 = a % 5
        num1 = str(num1)
        a = a//5
        num2 = num2 + num1
    return reverse(num2)

def gumatj_to_decimal(a):
    num1 = ""
    a = str(a)
    if a == 0:
        return 0
    if len(a) == 1:
        num1 = int(a)
    elif len(a) == 2:
        x = a[0]
        y = a[1]
        num1 = (int(x)*5) + (int(y) * 1)
    return num1

def gumatj_add(a,b):
    num1 = int(gumatj_to_decimal(a))
    num2 = int(gumatj_to_decimal(b))
    num3 = num1 + num2
    answer = decimal_to_gumatj(num3)
    return answer

def gumatj_multiply(a,b):
    if a == 0 or b == 0:
        return 0
    num1 = int(gumatj_to_decimal(a))
    num2 = int(gumatj_to_decimal(b))
    num3 = num1 * num2
    answer = decimal_to_gumatj(num3)
    return answer

