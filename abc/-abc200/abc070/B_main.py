a,b,c,d = map(int,input().split())

s = list(range(a,b))
t = list(range(c,d))

u = set(s) & set(t)

print(len(u))