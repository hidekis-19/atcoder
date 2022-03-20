n,k = map(int,input().split())
H = list(map(int,input().split()))

H = sorted(H,reverse=True)


if sum(H) <=k:
    print(sum(H))
else:
    s = 0

    for h in H[k:]:
        s += h
    print(s)


