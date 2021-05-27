n = int(input())
B = list(map(int,input().split()))

ans = B[0] + B[n-2]

for i in range(n-2):
    ans += min(B[i],B[i+1])

print(ans)


