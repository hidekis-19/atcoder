n = int(input())
A = list(map(int,input().split()))

ans = 0

for i in range(n-1):
    for j in range(i,n):
        ans = max(ans,abs(A[i]-A[j]))
print(ans)