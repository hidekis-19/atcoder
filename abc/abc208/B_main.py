import math
p = int(input())


x = 0

for i in range(1,13):
    if p < math.factorial(i):
        x = i
        break
l = list(range(1,x))
l = sorted(l,reverse=True)
ans = 0
for i in l:
    ans += p//math.factorial(i)
    p = p%math.factorial(i)
print(ans)


