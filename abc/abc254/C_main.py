from collections import deque
n,k = map(int,input().split())
A = list(map(int,input().split()))

B = sorted(A)

C = [[] for _ in range(k+1)]
D = []
for i,a in enumerate(A):
    i = i%k
    C[i+1].append(a)


for c in C:
    D.append(deque(sorted(c)))

for d in D:
    if len(d) ==0:
        D.remove(d)
E = []
cnt = 0
while cnt < n:
    E.append(D[cnt%k].popleft())
    cnt += 1

if B ==E:
    print("Yes")
else:
    print("No")    
    
    

