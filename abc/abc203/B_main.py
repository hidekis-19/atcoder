n,k  = map(int, input().split())
ans = 0
for i in range(1,n+1):
    for j in range(1,k+1):
        a = str(i)
        b = str(j)
        x = int(a+ '0'+b)
        ans += x
print(ans)