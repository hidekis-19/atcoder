n,t = map(int,input().split())
ctList= []
for i in range(n):
    ctList.append(list(map(int,input().split())))
    
ans = 999999999999

for c,tt in ctList:
    if tt <= t:
        ans = min(ans,c) 


if ans == 999999999999:
    print("TLE")
else:
    print(ans)