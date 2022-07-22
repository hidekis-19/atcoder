n,q = map(int,input().split())
lrtList = []

numList = [[0] for i in range(n+1)]

for i in range(q):
    lrtList.append(list(map(int,input().split())))
    
for l,r,t in lrtList:
    for i in range(l,r+1):
        numList[i] = t

for i,num in enumerate(numList):
    if i == 0:
        continue
    if num == [0]:
        print(0)
    else:    
        print(num)