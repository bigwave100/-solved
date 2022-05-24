n = int(input())
a = n//2

if (n%2 != 0) :
    b = n//2 + 1
else :
    b = n//2

if (n == 1) :
    print(1)
elif (n == 2) :
    print(1,2)
elif (n == 3) :
    print(1,2,3)
else :
    if (n%2 == 0) :
        while(b > 0) :
            if (b != 1) :
                print(b, b+a, end=' ')
            else :
                print(b, b+a)

            b -= 1
    else :
        while(b > 0) :
            if (b != 1) :
                print(b, b+a, end=' ')
            else :
                print(b)

            b -= 1
