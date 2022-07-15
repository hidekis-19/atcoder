n = int(input())
d,x = map(int,input().split())
A = []

for i in range(n):
    A.append(int(input()))
    
ans = x

for a in A:
    ans += 1
    ans += (d-1)//a
print(ans)


    