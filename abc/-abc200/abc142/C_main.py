n = int(input())
A = list(map(int,input().split()))
ans = [0]*n

for i,a in enumerate(A):
    ans[a-1] = i+1

L=[str(a) for a in ans]
L=" ".join(L)

print(L)
