n = int(input())
D = list(map(int,input().split()))

ans = 0

for i,d1 in enumerate(D):
    for j,d2 in enumerate(D):
        if i!=j:
            ans += d1 * d2
print(ans//2)