n = int(input())
tlr = []
for i in range(n):
    tlr.append(list(map(int,input().split())))

ans =0
for i in range(n-1):
    ti = tlr[i][0]
    li = tlr[i][1]
    ri = tlr[i][2]
    if ti==2:
        ri = ri - 0.1
    elif ti==3:
        li = li + 0.1
    elif ti==4:
        li = li + 0.1
        ri = ri - 0.1    
    for j in range(i+1,n) :
        tj = tlr[j][0]
        lj = tlr[j][1]
        rj = tlr[j][2]
        if tj==2:
            rj = rj - 0.1
        elif tj==3:
            lj = lj + 0.1
        elif tj==4:
            lj = lj + 0.1
            rj = rj - 0.1
        if ri < lj:
            continue
        elif li > rj:
            continue
        else :
            ans +=1

print(ans)