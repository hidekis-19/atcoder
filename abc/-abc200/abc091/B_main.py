import collections
n = int(input())
S = []

for i in range(n):
    S.append(input())
m = int(input())
T = []

for i in range(m):
    T.append(input())


c1 = collections.Counter(S)
c2 = collections.Counter(T)

ans =0
for c in c1:
    x = c1[c]
    y = c2[c]
    if x > y:
        ans = max(ans,x-y)

print(ans)