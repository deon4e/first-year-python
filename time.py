#Program to check validity of times enetered
#By Deon Fourie
#24 February

hours=eval(input("Enter the hours: "))
minutes=eval(input("Enter the minutes: "))
seconds=eval(input("Enter the seconds: "))

if hours<=23:
    if hours>=0:
        if minutes<=59:
            if minutes>=0:
                if seconds<=59:
                    if seconds>=0:
                        print("Your time is valid.")
                    else:
                        print("Your time is invalid.")
                else:
                    print("Your time is invalid.")
            else:
                print("Your time is invalid.")
        else:
            print("Your time is invalid.")
    else:
        print("Your time is invalid.")
else:
    print("Your time is invalid.")    
    
                    
                    
                    
                
            


        