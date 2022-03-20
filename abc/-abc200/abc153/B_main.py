h,n = map(int,input().split())
A = list(map(int,input().split()))


for a in A:
    h -= a
    if h<=0:
        print('Yes')
        exit()
print('No')