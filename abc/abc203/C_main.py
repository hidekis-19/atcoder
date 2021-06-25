n,k  = map(int, input().split())
ab_list = []

for i in range(n):
    ab_list.append(list(map(int,input().split())))

ab_list = sorted(ab_list)
l = 0

if k < ab_list[0][0]:
    print(k)
    exit()

for i in range(n):
    if i==0:
        k = k-ab_list[i][0]
    else:
        k -= ab_list[i][0] -ab_list[i-1][0]
    
    if k <0:
        print(ab_list[i-1][0]+l)
        aa = 1
        exit()
    k += ab_list[i][1]
    l = k

print(ab_list[n-1][0] +l)



