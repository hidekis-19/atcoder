n = int(input())
A = list(map(int,input().split()))

B = set()
C = set()
t=0

for j in range(n):
    if A[j] !=A[n-1-j]:
        B.add(A[j])
        C.add(A[n-1-j])
        t=1

if t==0:
    print(0)
else:
    x = max(len(B),len(C))
    D = B | C
    y = len(D)-1
    print(min(x,y))


