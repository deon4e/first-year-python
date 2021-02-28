#Program to calculate the area of a triangle given 3 side lengths
#By Deon Fourie
#24 February
from math import sqrt
a=eval(input("Enter the length of the first side: "))
b=eval(input("Enter the length of the second side: "))
c=eval(input("Enter the length of the third side: "))

s=(a+b+c)/2
area=sqrt(s*(s-a)*(s-b)*(s-c))
print("The area of the triangle with sides of length", a,"and", b,"and", c,"is", area, end=".")


