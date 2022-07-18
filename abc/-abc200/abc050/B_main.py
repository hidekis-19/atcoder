n = int(input())
T = list(map(int,input().split()))
m = int(input())
pxList = []

for i in range(m):
    pxList.append(list(map(int,input().split())))



sumT = sum(T)

for p,x in pxList:
    s = sumT + x - T[p-1]
    print(s)