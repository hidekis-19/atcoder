import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())

ab_list =[]

for i in range(m):
    ab_list.append(list(map(int,input().split())))

graph = [deque([]) for _ in range(N + 1)]
