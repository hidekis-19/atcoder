import collections

n = int(input())
A = list(map(int,input().split()))

c = collections.Counter(A)

sumA = 0

for v in c.items():
    sumA += (v[1] *(v[1]-1))/2
    
for k in range(n):
    sumC = sumA - c[A[k]] +1
    print(int(sumC))
