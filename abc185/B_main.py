N,M,T= map(int, input().split())
N_max = N
num_list = []
for i in range(M):
    num_list.append(list(map(int,input().split())))

ans = 'Yes'

for i,n in enumerate(num_list):
    if i==0:
        N -= n[0]
        if N<=0:
            ans = 'No'
            break
        N = min(N_max,N+n[1] -n[0])
    else:
        N-= num_list[i][0]-num_list[i-1][1]
        if N<=0:
            ans = 'No'
            break
        N = min(N_max,N+num_list[i][1] -num_list[i][0])

        

x = num_list[-1:]
if N -(T- x[0][1])<=0:
    ans = 'No'

print(ans)

