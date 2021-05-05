N = int(input())


A = []
B = []

ans = 9999999999999999
for i in range(N):
    a,b= map(int, input().split())
    A.append(a)
    B.append(b)


for i,a in enumerate(A):
    x = 999999999999
    if a<x:
        x = a
    for j,b in enumerate(B):
        y = 99999999999999999
        if b<y:
            y = b
        if (i!=j) and (max(x,y)<ans):
            ans = max(x,y)
        elif (i==j) and (x+y<ans):
            ans = x+y
print(ans)
        

