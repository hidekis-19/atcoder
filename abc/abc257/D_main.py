n = int(input())
xyp_list = []

for i in range(n):
    xyp_list.append(list(map(int,input().split())))
    
S = []

for a in xyp_list:
    x1 = a[0]
    y1 = a[1]
    p1 = a[2]
    v = 0
    for b in xyp_list:
        x2 = b[0]
        y2 = b[1]
        v = max(v,abs(x1-x2)+abs(y1-y2))
    S.append([p1,v])



print(S)
        
        
