from itertools import combinations
n = int(input())
A = list(map(int,input().split()))

B = [[] for i in range(2*10**5+1)]

for i,a in enumerate(A):
    B[a].append(i)

C = []

for b in B:
    if len(b)>0:
        C.append(len(b))

ans = 0

s = C[0]

for i in range(1,len(C)-1):
    ans += s * C[i] *(n-s-C[i])
    s += C[i]
print(ans)
    
