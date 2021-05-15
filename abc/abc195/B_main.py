A,B,W= map(int, input().split())

W = W*1000

ans_ng = 'UNSATISFIABLE'
ans = []
mikan = list(range(1,1000001))

for m in mikan:
    if A*m <= W <=B*m:
        ans.append(m)

if len(ans) > 0:
    print(min(ans),max(ans))
else:
    print(ans_ng)


