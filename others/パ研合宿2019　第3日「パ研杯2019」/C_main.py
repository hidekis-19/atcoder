n,m = map(int,input().split())
A = []

for i in range(n):
    A.append(list(map(int,input().split())))

ans = 0

for i in range(m):
    for j in range(m):
        x = 0
        if i == j:
            continue
        for k in range(n):
            x += max(A[k][i],A[k][j])
        ans = max(ans,x)
print(ans)
    



