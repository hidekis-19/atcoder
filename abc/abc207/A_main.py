a,b,c = map(int,input().split())

x = min(a,b,c)
y = [a,b,c]
print(sum(y)-x)
