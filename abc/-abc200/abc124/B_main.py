n = int(input())
H = list(map(int,input().split()))

ans = 0
maxh = H[0]

for h in H:
    if h >= maxh:
        ans += 1
        maxh = h
print(ans)