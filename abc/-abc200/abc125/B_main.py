n = int(input())
V = list(map(int,input().split()))
C = list(map(int,input().split()))

ans = 0
for i,v in enumerate(V):
    s = v -C[i]
    if s>=0:
        ans += s
print(ans)