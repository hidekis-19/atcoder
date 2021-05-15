n = int(input())

A = list(map(int, input().split())) 
C = A
y = 0

while len(A)>=2:
    if len(A) == 2:
        y = min(A)
    B = []
    for i in range(1,int(len(A)/2)+1):
        x = max(A[2*i-2],A[2*i-1])
        B.append(x)
    A = B

ans = C.index(y) +1
print(ans)


