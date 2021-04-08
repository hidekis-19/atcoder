N = int(input())
str_list = []
for i in range(N):
    str_list.append(list(input().split()))

ans_list = []

for i in str_list:
    if (int(i[2]) - int(i[0])) > 0:
        ans_list.append(int(i[1]))

if len(ans_list) > 0:
    ans = min(ans_list)
else:
    ans = -1

print(ans)

