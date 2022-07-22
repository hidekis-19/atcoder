n,x,y,z = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

AA = []
BB = []
CC = []

for i in range(n):
    CC.append([A[i]+B[i],i+1])



cnt = [0]*(n+5)
ans = []
for i,a in enumerate(A):
    AA.append([a,i+1])
    
for i,b in enumerate(B):
    BB.append([b,i+1])

AA = sorted(AA, key=lambda x:(-x[0],x[1]))
BB = sorted(BB, key=lambda x:(-x[0],x[1]))
CC = sorted(CC, key=lambda x:(-x[0],x[1]))
for a in AA:
    if len(ans) >= x :
        break
    if cnt[a[1]] == 0:
        ans.append(a[1])
        cnt[a[1]] = 1

for b in BB:
    if len(ans) >= y +x:
        break
    if cnt[b[1]] == 0:
        ans.append(b[1])
        cnt[b[1]] = 1

for c in CC:
    if len(ans) >= z +x + y:
        break
    if cnt[c[1]] == 0:
        ans.append(c[1])
        cnt[c[1]] = 1

for an in sorted(ans):
    print(an)
    





