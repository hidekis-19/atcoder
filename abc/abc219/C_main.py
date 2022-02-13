x = list(input())
n = int(input())
S = []

for i in range(n):
    S.append(input())

L =[]
for t,s in enumerate(S):
    a = []
    for i in s:
        a.append(x.index(i)+1)
    L.append([a,t])

L = sorted(L)

for l in L:
    print(S[l[1]])

