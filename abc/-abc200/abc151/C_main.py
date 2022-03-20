n,m = map(int,input().split())
P =[]

for i in range(m):
    P.append(list(map(str,input().split())))

ac =0
pe =0
N = [0]*10**5

for p in P:
    if N[int(p[0])] !=1:
        if p[1] == 'AC':
            ac +=1
            pe += abs(N[int(p[0])])
            N[int(p[0])] = 1 
        elif p[1] == 'WA':
            N[int(p[0])] = N[int(p[0])] -1
print(ac,pe)
    