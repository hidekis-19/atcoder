import math
n = int(input())
A = list(map(int,input().split()))

m = 0

for a in A:
    if a>0:
        m += 1


s = sum(A)/m
print(math.ceil(s))

