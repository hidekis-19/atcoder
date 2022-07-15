n = int(input())

ans = 0

for i in range(100000):
    x = i **2
    if n >=x:
        ans = x
    else:
        break
print(ans)