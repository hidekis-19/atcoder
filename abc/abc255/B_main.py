n,k = map(int,input().split())
A = list(map(int,input().split()))
xy_list = []

for i in range(n):
    xy_list.append(list(map(int,input().split())))
    
right = []
no_right = []

for i,xy in enumerate(xy_list):
    if i+1 in A:
        right.append(xy)
    else:
        no_right.append(xy)

ans = 0
for nr in no_right:
    s_list = []
    for r in right:
        s = ((nr[0]-r[0])**2 +(nr[1]-r[1])**2)**0.5
        s_list.append(s)
    ans = max(ans,min(s_list))
print(ans)
