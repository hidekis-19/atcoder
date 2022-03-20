n = int(input())
X = list(map(int,input().split()))

ans = 10000000000000000000000000000000000000000

for x in range(101):
    s = 0
    for y in X:
        s += (x-y)**2
    ans = min(ans,s)
print(ans)