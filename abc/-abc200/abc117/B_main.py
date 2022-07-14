n = int(input())
L = list(map(int,input().split()))


Lmax = max(L)
sumL = sum(L)

if Lmax < sumL - Lmax:
    print("Yes")
else:
    print("No")