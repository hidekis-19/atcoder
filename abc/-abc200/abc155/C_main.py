import collections

n = int(input())

S = []

for i in range(n):
    S.append(input())

c = collections.Counter(S)
c_max = c.most_common()[0][1]
s = []
for i in c.most_common():
    if i[1] == c_max:
        s.append(i[0])


for  i in sorted(s):
    print(i)