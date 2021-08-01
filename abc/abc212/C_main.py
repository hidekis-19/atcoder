import bisect
n,m = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A = sorted(A)
B = sorted(B)

ans = 999999999999999999999
y = 999999999999999999999

for a in A:
    s = bisect.bisect_left(B, a)
    x = abs(a-B[s-1])
    if s < m:
        y = abs(a-B[s])
    ans = min(ans,x,y)
print(ans)




