n = int(input())
A = list(map(int, input().split())) 

A = sorted(A)
ans = 0
su = sum(A)

for i in range(n):
    su -= A[i]
    ans += su  - (n-i-1)*A[i]
print(ans)
