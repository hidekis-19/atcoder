import numpy
from itertools import permutations
# インプット
N = int(input())

grid = []
for i in range(N):
    grid.append(list(map(int, input().split())) )

# ここに移動距離を入れていく
dis = []

per = permutations(grid,N)
for i in per:
    i_dis = 0
    for j in range(N-1):
        x = ((i[j][0]-i[j+1][0])**2 +(i[j][1]-i[j+1][1])**2)**0.5
        i_dis += x
    dis.append(i_dis)

print(sum(dis)/len(dis))
        












