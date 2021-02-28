n = int(input("Enter the start number: "))
if -6 < n < 2:
    for x in range(n,n+6):
        for j in range(7):
            if 0 <= n < 10:
                print("", n, end=" ")
            else:
                print(n, end=" ")
            n += 1
        print()
