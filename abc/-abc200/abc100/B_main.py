n,d = map(int,input().split())

if n==0:
    if d != 100:
        print(d)
    else:
        print(101)
elif n==1:
    if d != 100:
        print(d*100)
    else:
        print(10100)
        
elif n==2:
    if d != 100:
        print(d*10000)
    else:
        print(1010000)
    