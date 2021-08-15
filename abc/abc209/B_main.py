n,x = map(int,input().split())
A = list(map(int,input().split()))

y = 0

for i,a in enumerate(A):
    if i%2 ==1:
        y += a -1
    else:
        y += a
if x >=y:
    print('Yes')
else:
    print('No')

