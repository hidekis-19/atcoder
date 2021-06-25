n = int(input())
ab_list = []

for i in range(n):
    ab_list.append(list(map(int,input().split())))

men_ao = 0
men_taka = 0
men_all =[]
for i,ab in enumerate(ab_list):
    men_ao += ab[0]
    men_all.append(2*ab[0]+ab[1])

men_all = sorted(men_all, reverse=True)
for i in range(n+1):
    if men_taka -men_ao> 0:
        print(i)
        exit()
    men_taka += men_all[i]

    