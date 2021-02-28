N = eval(input("Enter the start point N: \n"))

M = eval(input("Enter the end point M: \n"))

print("The palindromic primes are: ")

N += 1
for i in range(N, M):
    bool_ = True
    if str(i) == str(i)[::-1]:
        if i >= 2:
            for a in range(2, i):
                if i % a == 0:
                    bool_ = False
                    break
            if bool_:
                print(i)
