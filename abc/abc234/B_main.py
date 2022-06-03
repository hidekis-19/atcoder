n = int(input())
xy_list = []
for i in range(n):
    xy_list.append(list(map(int,input().split())))
    
ans = 0
for xy1 in xy_list:
    for xy2 in xy_list:
        if xy1 != xy2:
            ans = max(ans,((xy1[0]-xy2[0])**2+(xy1[1]-xy2[1])**2)**0.5)
print(ans)
        
    