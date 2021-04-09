N,Y= map(int, input().split())

Y = Y/1000

ans = []

for i in range(N+1):
    money_1 = i*10
    money_1_1 = (N-i)*5
    if (money_1 == Y) and i == N:
        x = i
        y = 0
        z = 0
        ans.append([x,y,z])
    elif (Y - money_1 > 0) and (Y- money_1 - money_1_1<= 0):
        for j in range(N+1-i):
            money_2 = j*5
            money_2_2 = (N-i-j)*1
            if (money_1 + money_2 == Y) and (i+j == N):
                x = i
                y = j
                z = 0
                ans.append([x,y,z])
            elif (Y -money_1 - money_2 >0) and (Y - money_1 - money_2 -money_2_2 <= 0):
                a =  Y -money_1 - money_2
                if a == (N -i-j):
                    x = i
                    y = j
                    z = int(a)
                    ans.append([x,y,z])
if ans == []:
    x = -1
    y = -1
    z = -1
    ans.append([x,y,z])
    
print(ans[0][0],ans[0][1],ans[0][2])

