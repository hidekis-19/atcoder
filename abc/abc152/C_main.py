n = int(input())
P = list(map(int,input().split()))
ans = 0
q = 10000000000
for i,p in enumerate(P):
    q = min(q,p)
    if p <= q:
        ans +=1

print(ans)
