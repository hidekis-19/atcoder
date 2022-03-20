n = int(input())
A = list(map(int, input().split())) 
aa = 1

if A.count(0)>0:
    print(0)
    exit()
else:
    for a in A:
        aa *= a
        if aa > 10**18:
            print(-1)
            exit()

print(aa)