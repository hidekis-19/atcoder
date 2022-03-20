n,x,t= map(int, input().split())

y = 0

if n%x == 0:
    y = n/x
else:
    y = n//x+1
print(int(y*t))