# Program that prints 7 consecutive numbers
# By Deon Fourie
# 6 March

start = eval(input("Enter the start number: "))

for x in range(6):
              if start < 0:
                            print(start, end=" ")
                            start += 1
              elif -1 < start < 10: 
                            print("",start, end=" ")
                            start += 1
              else:
                            print(start, end=" ")
                            start+=1
if start == 0:
              print('', start)
elif 0 < start < 9:
              print("", start)
elif start == 9:
              print("", start)
elif start > 9:
              print(start)
