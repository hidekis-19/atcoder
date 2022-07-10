n,q = map(int,input().split())
ab_list = []
px_list = []
p_list = [0]*200010


# 深さ優先探索
import sys
input = sys.stdin.readline
from collections import deque

# グラフの作成
graph = [deque([]) for _ in range(n + 1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)  
    
for i in range(q):
    px_list.append(list(map(int,input().split())))
for px in px_list:
    p_list[px[0]] += px[1]

gone = set()

cnt = [0] * (n + 1)
# 深さ優先探索
def dfs(v):
    stack = [v]
    while stack:
        v = stack[-1]
        gone.add(v)
        cn = p_list[v]
        if graph[v]:
            w = graph[v].popleft()
            if w in gone:
                continue    
            cnt[w] += cn + cnt[v]
            stack.append(w) 
        else:
            z= stack.pop()
            cnt[z] += p_list[z]  
    return cnt

# 孤立している頂点対策
for i in range(n):
    if cnt[i + 1] == 0:
        ans = dfs(i + 1)

print(* cnt[1:])