N = int(input())

d = []
ans = 0

for key in range(1,N+1):
    A = int(input())
    x = []
    for j in range(A):
        x.append(list(input().split()))
    d.append(x)    

num = list(range(1,N+1))


for i in range(2 ** N):
    x = [0]*N
    for j in range(N):  
        if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
            x[j] = 1
    flag = True
    for i,s in enumerate(x):
        if s==1:
            for (a,b) in d[i]:
                if x[int(a)-1] != int(b):
                    flag = False
    if flag :
        ans = max(ans,sum(x))

print(ans)


