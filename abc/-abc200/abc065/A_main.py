x,a,b = map(int,input().split())


if b<=a :
    print("delicious")
elif b <= x+a:
    print("safe")
else:
    print("dangerous")