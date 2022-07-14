x = int(input())

ans = 0
for i in range(1,1010):
    for j in range(2,15):
        y = i**j
        if x >= y:
            ans = max(ans,y)

print(ans)