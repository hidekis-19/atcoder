n = int(input())
H = list(map(int,input().split()))

ans =0
x = 0
for i in range(n-1):
    if H[i] >= H[i+1]:
        x += 1
    else:
        ans = max(ans,x)
        x = 0
    ans = max(ans,x)

print(ans)
        