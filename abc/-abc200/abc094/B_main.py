n,m,x = map(int,input().split())
A = list(map(int,input().split()))

s = set(list(range(1,x)))
t = set(list(range(x+1,n+1)))

ans = min(len(set(A)&set(s)),len(set(A)&set(t)))

print(ans)

