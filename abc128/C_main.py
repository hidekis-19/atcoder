from collections import defaultdict
from itertools import product
 
N, M = map(int, input().split())
 
d = defaultdict(set)
res = 0
 
for key in range(1, M+1): # keyは電球を指定
    l = list(map(int, input().split()))
    l.pop(0)
    for i in l:
        d[key].add(i)  # dict = {(電球番号(key): [スイッチ番号(i), ...],...}
 
p = list(map(int, input().split()))
 
for a in product(*((0, x) for x in range(1, N+1))):
    light = 0 # 光っている電球の個数
    for key in range(1, M+1):
        count = len(d[key] & set(a)) # 電球番号(key)のスイッチがONになっている個数
        if count%2 == p[key-1]:
            light += 1
    if light == M:
        res += 1
 
print(res)