n,k  = map(int, input().split())
A = []

for i in range(n):
    A.append(list(map(int,input().split())))

ans = 10000000000
for i in range(n-k+1):
    for j in range(n-k+1):
        x = []
        for s in range(k):
            x.extend(A[i+s][j:j+k])
        x = sorted(x,reverse=True)
        ans = min(ans,x[int(k**2/2)])
print(ans)


                