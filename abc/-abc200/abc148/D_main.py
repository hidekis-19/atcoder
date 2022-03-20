n = int(input())
A = list(map(int,input().split()))


ans = 0
s = 1
for i,a in enumerate(A):
    if a ==s:
        s += 1
    else:
        ans +=1

if s-1:
    print(ans)
else:
    print(-1)

