N = input()
n_len = len(N)

ans = 0

if n_len==2:
    x = int(N[0])
    y = int(N[1])
    if x<=y:
        ans = x
    elif x>=y:
        ans = x-1
        
elif n_len==3:
    ans = 9
elif n_len==4:
    ans = 9
    x = int(N[:2])
    y = int(N[2:])
    if x<=y:
        ans += x -10 +1
    else:
        ans += x -10 +1 -1
elif n_len==5:
    ans = 99
elif n_len==6:
    ans = 99
    x = int(N[:3])
    y = int(N[3:])
    if x<=y:
        ans += x -100 +1
    else:
        ans += x -100 +1 -1
elif n_len==7:
    ans = 999
elif n_len==8:
    ans = 999
    x = int(N[:4])
    y = int(N[4:])
    if x<=y:
        ans += x -1000 +1
    else:
        ans += x -1000 +1 -1
elif n_len==9:
    ans = 9999
elif n_len==10:
    ans = 9999
    x = int(N[:5])
    y = int(N[5:])
    if x<=y:
        ans += x -10000 +1
    else:
        ans += x -10000 +1 -1
elif n_len==11:
    ans = 99999
elif n_len==12:
    ans = 99999
    x = int(N[:6])
    y = int(N[6:])
    if x<=y:
        ans += x -100000 +1
    else:
        ans += x -100000 +1 -1
print(ans)



