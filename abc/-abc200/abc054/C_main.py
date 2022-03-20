from itertools import permutations
N,M= map(int, input().split())

num_list = []
for i in range(M):
    num_list.append(list(map(int,input().split())))

ans = 0
n_list = list(range(1,N+1))

per = permutations(n_list,N)
for i in per:
    x = list(i)
    flag = True
    if x[0] == 1:
        for j in range(len(x)-1):
            y = [x[j],x[j+1]]
            z = [x[j+1],x[j]]

            if  (not y in num_list) and (not z in num_list):
                flag = False
                break
        if flag:
            ans += 1
print(ans)

                