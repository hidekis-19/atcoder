n = int(input())
C= list(map(int,input().split()))

if n > max(C):
    print(0)
    exit()
ans =1
D = sorted(C)

for i,c in enumerate(D):
    x = c - i 
    ans = (ans*x)%(10**9+7)
print(ans)


