import bisect
H,W,N = map(int,input().split())
AB_list = []
A = []
B = []
for i in range(N):
    a,b = map(int,input().split())
    AB_list.append([a,b])
    A.append(a)
    B.append(b)

A = sorted(list(set(A)))
B = sorted(list(set(B)))

for ab in AB_list:
    # indexよりもbisect使ったほうが早い
    s = bisect.bisect(A,ab[0])
    t = bisect.bisect(B,ab[1])
    print(s,t)
