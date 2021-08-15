n,k = map(int,input().split())
A = list(map(int,input().split()))

B = sorted(A)

x = k//n
y = k - x*n
z = B[y-1]


for a in A:
    if y != 0:
        if a <= z:
            print(x+1)
        else:
            print(x)
    else:
        print(x)

