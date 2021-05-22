n,k,m = map(int,input().split())
A = list(map(int,input().split()))

if m*n-sum(A) <=k:
    if m*n-sum(A) >=0:
        ans = m*n-sum(A)
    else:
        ans = 0
else:
    ans = -1
print(ans)
