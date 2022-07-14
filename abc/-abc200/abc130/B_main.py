n,x = map(int,input().split())
L =list(map(int,input().split()))

boul = [0]
ins = 0
for l in L:
    ins= ins+l
    boul.append(ins)
    

ans = 0

for b in boul:
    if b <= x:
        ans += 1
print(ans)