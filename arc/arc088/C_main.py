x,y = map(int,input().split())
ans = 0
for i in range(1000):
    if x*2**i <= y:
        ans +=1
print(ans)

