import collections
n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

D = []
for c in C:
    D.append(B[c-1])

cA = [0]*n
cD = [0]*n

for i in range(n):
    cA[A[i]-1] +=1
    cD[D[i]-1] +=1

ans = 0
for i in range(n):
    ans += cA[i] * cD[i]
print(ans)

