import itertools

N = int(input())
ans = 'No'
num_list = []
for i in range(N):
    num_list.append(list(map(int,input().split())))


for v in itertools.combinations(num_list,3):
    v = list(v)
    if v[0][0] == v[1][0] and v[1][0] == v[2][0]:
        ans = 'Yes'
        break
    elif v[0][0] != v[1][0]:
        m = (v[1][1]-v[0][1])/(v[1][0]-v[0][0])
        P = m*(v[2][0]-v[0][0]) + v[0][1] - v[2][1]
        if P ==0:
            ans = 'Yes'
            break
print(ans)

