n,q = map(int,input().split())

x_list = []

for i in range(q):
    x_list.append(int(input()))
    
val = list(range(1,n+1))
pos = list(range(1,n+1))

for x in x_list:
    s = pos[x-1] -1
    if s != n-1:
        val[s+1],val[s] = x,val[s+1]
        pos[val[s]-1],pos[val[s+1]-1] = pos[val[s+1]-1],pos[val[s]-1]
    else:
        val[s],val[s-1] = val[s-1],x
        pos[val[s]-1],pos[val[s-1]-1] = pos[val[s-1]-1],pos[val[s]-1]

print(' '.join(map(str,val)))
