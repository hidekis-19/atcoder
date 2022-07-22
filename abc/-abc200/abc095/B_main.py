n,x = map(int,input().split())
M = []

for i in range(n):
    M.append(int(input()))
    
ans = n
x = x - sum(M)
Mmin = min(M)

while x :
    x = x -  Mmin
    if x >= 0:
        ans += 1
    else:
        break

print(ans)

