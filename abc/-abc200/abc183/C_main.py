import itertools
n,k= map(int, input().split())

num_list = []
for i in range(n):
    num_list.append(list(map(int,input().split())))

n_list = list(range(2,n+1))


p = itertools.permutations(n_list, n-1)
ans =0
for i in p:
    x = 0
    i = list(i)
    i = [1] + i
    i.append(1)
    il = len(i)
    for j in range(il-1):
        y =  i[j]
        z =  i[j+1]
        x += num_list[y-1][z-1]
    if x== k:
        ans += 1

print(ans)        
    