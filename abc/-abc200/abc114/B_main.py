s = input()

t = []

for i in range(1,len(s)-1):
    t.append(int(s[i-1]+s[i]+s[i+1]))
ans = 9999999999

for tt in t:
    ans = min(abs(753-tt),ans)

print(ans)
