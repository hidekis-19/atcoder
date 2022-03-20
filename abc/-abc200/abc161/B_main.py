n,m = map(int,input().split())
A  = list(map(int,input().split()))

x = 0

A_sum = sum(A)

for a in A:
    if 4*a*m >= A_sum:
        x += 1

if x >= m:
    print('Yes')    
else:
    print('No')