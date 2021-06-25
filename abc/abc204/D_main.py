n = int(input())
T = list(map(int,input().split()))

T = sorted(T,reverse=True)
ans =0
while len(T) >=1:
    t= T[0]
    ans += t
    x = 0
    T.remove(t)
    while True:
        v = -1
        for s in T:
            if s <= t:
                v = max(v,s)
        if v==-1:
            break
        t -= v
        if t <0:
            break
        else:
            T.remove(v)
print(ans)



        



