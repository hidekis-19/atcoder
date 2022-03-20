a,b = map(int,input().split())

x = [a]*b
y = [b]*a

x=[str(a) for a in x]
x="".join(x)
y=[str(a) for a in y]
y="".join(y)

s = min(x,y)
print(s)

