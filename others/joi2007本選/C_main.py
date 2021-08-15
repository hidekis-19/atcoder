from itertools import combinations
N = int(input())
L = []


for _ in range(N):
    x,y = map(int,input().split())
    L.append((x,y))
L = set(L)
ans = 0
for p1,p2 in combinations(L,2):
    p3 = (p1[0] + p2[1] - p1[1],p1[1] - p2[0] + p1[0])
    p4 = (p2[0] + p2[1] - p1[1],p2[1] - p2[0] + p1[0])
    if (p3 in L) and (p4 in L):
        ans = max(ans,(p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
print(ans)
