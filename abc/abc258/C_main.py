n,q = map(int,input().split())
S = list(input())

a = 0

for i in range(q):
    t,x = map(int,input().split())
    if t == 1:
        a += x
        a = a%n
    elif t==2:
        s = x-1 - a
        if s <0:
            s += n
        print(S[s])
