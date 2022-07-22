o = input()
e = input()

ans = ""

s = len(o)
t = len(e)

for i in range(s):
    ans = ans + o[i]
    if i == s-1 and  s > t:
        break
    ans = ans + e[i]
print(ans)
