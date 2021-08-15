n,k = map(int,input().split())
C = list(map(int,input().split()))

ans =0
x = C[0:k]
ans = len(set(x))
for i in range(n-k+1):
    x.pop(0)
    if C[i+k-1] not in set(x):
        ans = max(len(set(x)) + 1,ans)
    x.append(C[i+k-1])
print(ans)