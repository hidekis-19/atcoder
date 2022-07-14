import itertools
a = int(input())
b = int(input())
d = int(input())
e = int(input())
c = int(input())

S = [a,b,c,d,e]
P = itertools.permutations(S, 5)

ansList = []

for pp in P:
    ans =0
    for i,p in enumerate(pp):
        if p%10==0 or i==4:
            ans += p
        else:
            ans += p - p%10 + 10
    ansList.append(ans)
print(min(ansList))   
    