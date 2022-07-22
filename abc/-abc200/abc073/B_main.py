n = int(input())
lrList = []

for i in range(n):
    lrList.append(list(map(int,input().split())))
    
ans = 0

for l,r in lrList:
    ans += r-l +1
print(ans)
