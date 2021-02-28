#Program to generate a spam message based off input
#Deon Fourie
#24 February

name=input("Enter first name:"'\n')
surname=input("Enter last name:"'\n')
money=eval(input("Enter sum of money in USD:"'\n'))
country=input("Enter country name:"'\n')
money30=(money*0.3)

print(" ")
print("Dearest",name)
print("It is with a heavy heart that I inform you of the death of my father,")
print("General Fayk",surname, end=",")
print(" your long lost relative from Mapsfostol.")
print("My father left the sum of ",end="")
print(money, " for us, your distant cousins.", sep="USD")
print("Unfortunately, we cannot access the money as it is in a bank in", country, end='.')
print('\n',"I desperately need your assistance to access this money.", sep="")
print("I will even pay you generously, 30% of the amount -", money30, end='USD,''\n')
print("for your help.  Please get in touch with me at this email address asap.")
print("Yours sincerely")
print("Frank",surname)






