from collections import deque
n,k = map(int,input().split())
C = list(map(int,input().split()))

D = []
for i,c in enumerate(C):
    D.append([i,c])
E = set(C)

for i in range(n):
    if D[i][1] in E:
        D.pop(i)


