N = int(input())

num_list = []
for i in range(N):
    num_list.append(list(map(int,input().split())))

ans = 0

for i in range(N-1):
    a = num_list[i]
    for j in range(i+1,N):
        b = num_list[j]
        x = a[0] -b[0]
        y = a[1] -b[1]
        if abs(y/x) <= 1:
            ans +=1
print(ans)



