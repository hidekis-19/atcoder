from collections import deque
n,w = map(int,input().split())
A = list(map(int,input().split()))

ans = deque()

for a in A :
    if a <= w:
        ans.append(a)

for i,a in enumerate(A):
    for j,b in enumerate(A):
        if (i<j) and (a+b<=w):
            ans.append(a+b)  
                   
for i,a in enumerate(A):
    for j,b in enumerate(A):
        for k,c in enumerate(A):
            if (i<j) and (j<k) and (a+b+c <= w):
                ans.append(a+b+c)

print(len(set(ans)))  
