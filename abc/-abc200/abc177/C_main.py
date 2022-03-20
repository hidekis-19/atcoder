n = int(input())
A = list(map(int, input().split())) 
ans = 0
a = 0

for i in range(n-1):
    a += A[i]
    ans += A[i+1]*a

ans = ans%1000000007
print(ans)