import collections

n = int(input())
A = list(map(int,input().split()))
c = collections.Counter(A)

if c.most_common()[0][1] >=2:
    print('NO')
else:
    print('YES')