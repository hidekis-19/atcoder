n = int(input())
A = list(map(int,input().split()))

A = sorted(A,reverse=True)
ans = 0

for i in range(n-1):
    ans += A[i] - A[i+1]
print(ans)