n,q = map(int,input().split())

x_list = []

for i in range(q):
    x_list.append(int(input()))
    
ans_list = list(range(1,n+1))

for x in x_list:
    s = ans_list.index(x)
    if s != n-1:
        ans_list[s+1],ans_list[s] = x,ans_list[s+1]
    else:
        ans_list[s],ans_list[s-1] = ans_list[s-1],x

print(' '.join(map(str,ans_list)))
