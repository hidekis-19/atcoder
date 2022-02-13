import math
n,m = map(int,input().split())
A = list(map(int,input().split()))
L = list(range(1,m+1))
L = set(L)

def prime_decomposition(N):
    S=list(range(2,N+1))
    p=list()
    while S[0]**2<=N:
        tmp=S[0]
        p.append(tmp)   
        S=[e for e in S if e%tmp!=0]
    return p+S

B =[]
for a in A:
    if a ==1:
        continue
    B.extend(prime_decomposition(a))
B = set(B)

for b in B:
    if b in L:
        for j in range(b,m+1,b):
            if j in L:
                L.remove(j)

print(len(L))
for l in L:
    print(l)


