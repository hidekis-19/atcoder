n = int(input())
ab_list= []
num_list = [[] for i in range(n+1)]
for i in range(n-1):
    ab_list.append(list(map(int,input().split())))
    
for ab in ab_list:
    a = ab[0]
    b = ab[1]
    num_list[a].append(b)
    num_list[b].append(a)

for num in num_list:
    if len(num) == n-1:
        print("Yes")
        exit()

print("No")
