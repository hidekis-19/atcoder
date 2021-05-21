n,a,b = map(int,input().split())

x = n//(a+b)
y = n%(a+b)

ans = x*a + min(y,a)
print(ans)