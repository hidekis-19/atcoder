n,m = map(int,input().split())
ab_list = []
cd_list = []

for i in range(n):
    ab_list.append(list(map(int,input().split())))

for i in range(m):
    cd_list.append(list(map(int,input().split())))


for ab in ab_list:
    x = 1000000000
    ans = 0
    for i,cd in enumerate(cd_list):
        y = abs(ab[0]-cd[0]) + abs(ab[1]-cd[1])
        if y < x:
            ans = i+1
            x = y
    print(ans)
    