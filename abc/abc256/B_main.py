n = int(input())
A = list(map(int,input().split()))

p = 0

for i,a in enumerate(A):
    if sum(A[i:])>=4:
        p += 1
print(p)