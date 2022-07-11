n = int(input())
W = list(map(int,input().split()))

ans = 999999999999999
s = sum(W)
t = 0
for w in W:
    s -= w
    t += w
    ans = min(ans,abs(s-t))

print(ans)    
