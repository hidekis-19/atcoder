n = int(input())
P = list(map(int,input().split()))

Q = sorted(P)
cnt =0
for i,p in enumerate(P):
    if p != Q[i]:
        cnt += 1

if cnt == 0 or cnt==2:
    print("YES")
else:
    print("NO")