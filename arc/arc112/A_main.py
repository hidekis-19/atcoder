t = int(input())
case = []
for i in range(t):
    case.append(list(map(int,input().split())))

for c in case:
    x = c[0]
    y = c[1]
    z = y - x -(x-1)
    if z<0:
        print(0)
    else:
        print(z*(z+1)//2)
    

