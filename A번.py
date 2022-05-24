n = int(input())
s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

line = input()
tot = 1
flag = 0

for i in range(1,n) :
    if (abs(s.index(line[i]) - s.index(line[i-1])) == 1) :
        tot += 1
    else :
        tot = 1

    if (tot >= 5) :
        flag = 1
        break

if (flag == 1) :
    print('YES')
else :
    print('NO')
