n,d,h= map(int, input().split())

ans = 0
num_list = []
for i in range(n):
    num_list.append(list(map(int,input().split())))

for i in num_list:
    x = i[0]
    y = i[1]
    ans = max(ans,((y-h)*x)/(d-x) + y)
print(ans)



