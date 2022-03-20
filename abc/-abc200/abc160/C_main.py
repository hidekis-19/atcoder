k,n = map(int,input().split())
A = list(map(int,input().split()))

dis = 0
y = 0
for i in range(n):
    if i == 0:
        x = A[i]
    if i == n-1:
        x = k - A[i] + A[0]
    else:
        x = A[i+1] - A[i]
    dis += x
    if y < x:
        y = x

print(dis-y)
