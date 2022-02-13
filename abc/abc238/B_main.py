n = int(input())
A = list(map(int, input().split())) 

L =[0,360]
s =0

for a in A:
    s += a
    if s >= 360:
        s -= 360
    L.append(s)
L = sorted(L)

ans =L[1]-L[0]

for i in range(len(L)-1):
    ans = max(ans,L[i+1]-L[i])
print(ans)