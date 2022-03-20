from collections import deque

n,m= map(int, input().split())
H = list(map(int, input().split())) 

n_list = list(range(1,n+1))

d = deque()
for i in range(m):
    a,b =map(int,input().split())
    d.extend([a,b])


x = n - len(set(n_list) & set(d))

print(m+x)

