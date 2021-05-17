dellist = lambda items, indexes: [item for index, item in enumerate(items) if index not in indexes]

H,W,K= map(int, input().split())
ans =0
C = []
for i in range(H):
    C.append(list(input()))

h = list(range(H))
w = list(range(W))
X =[]
Y =[]

for i in range(2 ** H):
    bag = []
    for j in range(H):  # このループが一番のポイント
        if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
            bag.append(h[j])  # フラグが立っていたら bag に果物を詰める
    X.append(bag)

for i in range(2 ** W):
    bag = []
    for j in range(W):  # このループが一番のポイント
        if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
            bag.append(w[j])  # フラグが立っていたら bag に果物を詰める
    Y.append(bag)

for x in X:
    s = 0
    D = dellist(C,x)
    for d in D:
        s += d.count('#')
    for y in Y:
        t = 0
        for yy in y:
            yyy = [r[yy] for r in D]
            t += yyy.count('#')
        if s-t == K:
            ans +=1
print(ans) 

        




