n = int(input())
A = list(map(int,input().split()))

for i in range(1,n+1):
    if A.count(i) != 1:
        print('No')
        exit()
print('Yes')


