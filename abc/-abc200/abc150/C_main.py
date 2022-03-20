import itertools
n = int(input())
p = list(map(int,input().split()))
q = list(map(int,input().split()))

S = itertools.permutations(list(range(1,n+1)))
a = 0
b = 0
for i,s in enumerate(S):
    if list(s) == p:
        a = i
    if list(s) == q:
        b = i
print(abs(a-b))