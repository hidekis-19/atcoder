n,m = map(int,input().split())

abList = []

for i in range(m):
    abList.append(list(map(int,input().split())))
    
toshi = [[] for i in range(n+5)]

for a,b in abList:
    toshi[a].append(b)
    toshi[b].append(a)


for i in range(1,n+1):
    print(len(toshi[i]))