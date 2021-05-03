N = int(input())

A = list(map(int, input().split())) 

ans = 0
for l in range(0,N):
    i = A[l]
    for r in range(l,N):
        i = min(i,A[r])
        ans = max(ans,(r-l+1)*i)
print(ans)



