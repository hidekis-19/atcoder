from collections import deque
n = int(input())
sx,sy,tx,ty = map(int,input().split())

xyr_list =[]
graph = [deque([]) for _ in range(n + 1)]
for i in range(n):
    xyr_list.append(list(map(int,input().split())))
R = [False for _ in range(n)]
#交点が何番目にあるか

ss = 99999999999999999999999999
tt = 99999999999999999999999999

for i,xyr1 in enumerate(xyr_list):
    x1 = xyr1[0] 
    y1 = xyr1[1]
    z1 = xyr1[2]
    if (sx-x1)**2 + (sy-y1)**2 == z1**2:
        ss = i
    if (tx-x1)**2 + (ty-y1)**2 == z1**2:
        tt = i
    for j,xyr2 in enumerate(xyr_list):
        x2 = xyr2[0] 
        y2 = xyr2[1]
        z2 = xyr2[2]
        d = (x1-x2)**2 + (y1-y2)**2
        if (xyr1 != xyr2) and (z1-z2)**2 <= d <= (z1+z2)**2:            
            graph[i].append(j)

def dfs(v):
    stack = [v]
    while stack:
        w = stack.pop()
        if w == tt:
            print("Yes")
            exit()
        R[w] = True
        for c in graph[w]:
            if not R[c]:
                stack.append(c)

dfs(ss)
print("No")