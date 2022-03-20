n,m = map(int,input().split())
sc_list = []

if m==0:
    if n==2:
        print(10)
    elif n==3:
        print(100)
    elif n==1:
        print(0)
    exit()

for i in range(m):
    sc_list.append(list(map(int,input().split())))

for i in range(1001):
    t = 0
    for j in sc_list:
        s = j[0] -1
        c = j[1] 
        if len(str(i))==n  and  str(i)[s] ==str(c):
            t += 1
    if t==m:
        print(i)
        exit()
print(-1)
