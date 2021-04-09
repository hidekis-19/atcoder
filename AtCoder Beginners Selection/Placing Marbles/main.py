s = input()

s_list = list(s)

ans = 0

for i in s_list:
    if i == '1':
        ans += 1

print(ans)
