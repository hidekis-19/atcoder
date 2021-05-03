N,M= map(int, input().split())

A = list(map(int, input().split())) 

A = sorted(A)
siro = 0
k = 99999999999999
for i in range(M-1):
    if not A[i+1]-A[i]==1:
        k = min(k,A[i+1]-A[i]-1)
        siro += A[i+1]-A[i]-1

if A[-1]!=N:
    k = min(k,N-A[-1])
    siro+= N-A[-1]
if A[0]!=1:
    k = min(k,A[0]-1)
    siro+= A[0]-1


print(siro)
print(k)
print(A)
