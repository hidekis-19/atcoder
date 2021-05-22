a,b,c,d = map(int,input().split())

for i in range(100000):
    a -= d
    c -= b
    if c<=0:
        print('Yes')
        exit()
    if a<=0:
        print('No')
        exit()
    