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

num = list(range(1,N+1))

for i in range(2 ** N):
    switchs = []
    for j in range(N):  
        if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
            switchs.append(num[j])  
    right = 0
    #ライトがつくかどうかを１つずつ確認する
    for k in range(1,M+1):
        x = len(set(d[k]) & set(switchs) )
        if len(set(d[k]) & set(switchs) )%2 == p[k-1]:
            right += 1
    if right == M:
        res +=1
print(res)
    







        





    
