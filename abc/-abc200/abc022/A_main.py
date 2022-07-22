n,s,t = map(int,input().split())
w = int(input())
A = []

for i in range(n):
    A.append(int(input()))
    
ans = 0

if  s <= w <= t:
    ans = 1

for a in A:
    w += a
    if s <= w <= t:
        ans += 1
print(ans)
    
