import numpy as np

def getNearestValue(list, num):

    # リスト要素と対象値の差分を計算し最小値のインデックスを取得
    idx = np.abs(np.asarray(list) - num).argmin()
    return list[idx]

n,m = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A = sorted(A)
B = sorted(B)

ans = 999999999999999999999

for a in A:
    b = getNearestValue(B,a)
    ans = min(ans,abs(a-b))
print(ans)




