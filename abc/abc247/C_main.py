n = int(input())

s_list =[["1"]]

for i in range(2,17):
    x = s_list[i-2] 
    x = x + [str(i)] 
    x = x + s_list[i-2]
    s_list.append(x)

ans = s_list[n-1]
L = ' '.join(map(str,ans))

print(L)
