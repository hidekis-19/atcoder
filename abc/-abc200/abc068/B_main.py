n = int(input())
ans = 1

for i in range(15):
    x = 2 ** i
    if x <= n:
        ans = x
    else:
        break
print(ans)