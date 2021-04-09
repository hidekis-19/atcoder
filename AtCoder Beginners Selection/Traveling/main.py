N = int(input())
num_list = []
for i in range(N):
    num_list.append(list(map(int,input().split())))

ans = 0
x0 = 0
y0 = 0
t0 = 0
for num in num_list:
    t = num[0]
    x = num[1]
    y = num[2]

    x_dis = abs(x0-x)
    y_dis = abs(y0-y)
    t_dis = t -t0
    if ((t_dis-x_dis-y_dis)%2==0) and (t_dis>=x_dis+y_dis):
        ans += 1
    
    x0 = x
    y0 = y
    t0 = t

if ans ==N:
    print('Yes')
else:
    print('No')



