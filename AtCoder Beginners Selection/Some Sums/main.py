N,A,B= map(int, input().split())

N_list = []

for i in range(N+1) :
    x = list(str(i))
    l_x = [int(s) for s in x]
    x_sum = sum(l_x)
    if (x_sum >= A) and (x_sum<= B):
        N_list.append(i)
print(sum(N_list))
