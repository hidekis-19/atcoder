n,k,q = map(int,input().split())
A = []
for i in range(q):
    A.append(int(input()))

men = [0]*n

for a in A:
    men[a-1] += 1
for m in men:
    if k-q+m >0:
        print('Yes')
    else:
        print('No')



