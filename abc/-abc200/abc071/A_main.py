x,a,b = map(int,input().split())

s = abs(x-a)
t = abs(x-b)

if s<t:
    print("A")
elif s>t:
    print("B")