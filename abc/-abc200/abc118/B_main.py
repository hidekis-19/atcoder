n,m = map(int,input().split())
kaList = []
for i in range(n):
    kaList.append(list(map(int,input().split())))

food = [0]*(m+1)

for ka in kaList:
    f = ka[1:]
    for ff in f:
        food[ff] = food[ff]+1

ans = 0
for i,f in enumerate(food):
    if f==n:
        ans+= 1
        
print(ans)
    
    

