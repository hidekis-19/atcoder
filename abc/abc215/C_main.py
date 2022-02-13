import itertools
s,k = input().split()
s = list(s)
k = int(k)

p = itertools.permutations(s, len(s))
p = set(list(p))

l = []


for i in p:
    l.append(''.join(i))
l = sorted(l)
print(l[k-1])
