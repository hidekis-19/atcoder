H,W= map(int, input().split())
num_list = []
for i in range(H):
    num_list.append(list(map(int,input().split())))


a_min = 99999999999
ans = 0
for i in num_list:
    a_min = min(a_min,min(i))


for i in num_list:
    for j in i:
        ans += j - a_min

print(ans)
