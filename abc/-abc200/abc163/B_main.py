n,m = map(int,input().split())

A = list(map(int, input().split())) 
ans = 0
if sum(A) > n:
    ans =-1
else:
    ans = n - sum(A)
print(ans)


