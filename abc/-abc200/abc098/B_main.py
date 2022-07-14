n = int(input())
s = list(input())

ans = 0


for i in range(1,n-1):
    t = s[i:]
    u = s[:i]
    ans = max(ans,len(set(t)&set(u)))
print(ans)