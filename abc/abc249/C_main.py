import itertools
import collections
n,k = map(int,input().split())
S = []
for i in range(n):
    S.append(input())

ans =0

for i in range(1,n+1):
    C = itertools.combinations(S,i)
    for c in list(C):
        x = 0
        L=list(''.join(list(c)))
        cnt = collections.Counter(L)
        x = list(cnt.values()).count(k)
        ans = max(ans,x)
        
print(ans)