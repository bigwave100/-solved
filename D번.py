n = int(input())
L = list(map(int,input().split()))
flag = 1
s = sum(L)
a = s//2

for k in L :
    if (k > a) :
        flag = 0
        break
if (n==1 and L[0]==1) :
    print('Happy')
elif (flag == 1) :
    print('Happy')
else :
    print('Unhappy')
