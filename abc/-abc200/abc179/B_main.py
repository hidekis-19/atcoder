n = int(input())
ans = 'No'
num_list = []
for i in range(n):
    a,b= map(int, input().split())
    if a == b:
        num_list.append(i)
if len(num_list)>=3:
    for i in range(len(num_list)-2):
        if num_list[i]- num_list[i+1]==-1 and num_list[i+1]-num_list[i+2]==-1:
            ans = 'Yes'
print(ans)
