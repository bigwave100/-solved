T = int(input())

for _ in range(T) :
    flag = 0
    L = list(input().split())
    L[0] = L[0][::-1]
    L[1] = L[1][::-1]
    L[2] = L[2][::-1]
    L[3] = L[3][::-1]
    L.sort()

    if (L[0]==L[1]==L[2] or L[1]==L[2]==L[3]) :
        flag = 1
    

    elif (L[0]==L[1] and L[2]==L[3]) :
        flag = 1

    else :
        
        if ((L[0][0]==L[1][0]==L[2][0]==L[3][0]) and (L[1][1]==L[2][1])) :
            a = int(L[0][1]) ; b = int(L[1][1]) ; c = int(L[3][1])

            if (a+1==b and b+1==c) :
                flag = 1

        if (L[0][0]==L[1][0]==L[2][0]) :
            a = int(L[0][1]) ; b = int(L[1][1]) ; c = int(L[2][1])

            if (a+1==b and b+1==c) :
                flag = 1

        if (L[1][0]==L[2][0]==L[3][0]) :
            a = int(L[1][1]) ; b = int(L[2][1]) ; c = int(L[3][1])

            if (a+1==b and b+1==c) :
                flag = 1

    if (flag == 1) :
        print(':)')
    else :
        print(':(')
