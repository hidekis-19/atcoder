n = int(input())
k = int(input())
x = int(input())
y = int(input())

if n <= k:
    print(x*n)
else:
    s = x*k
    t = y*(n-k)
    print(s+t)