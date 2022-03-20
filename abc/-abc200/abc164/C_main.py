from collections import deque
n = int(input())

ans = 0
d = deque()

for i in range(n):
    d.append(input())


y = list(set(d))
print(len(y))
