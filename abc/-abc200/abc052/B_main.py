n = int(input())
S = list(input())

x = 0
ans = 0

for s in S:
    if s == "I":
        x += 1
    elif s == "D":
        x -= 1
    if ans <= x:
        ans = x
print(ans)