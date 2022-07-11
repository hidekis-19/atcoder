n = int(input())
sp_list = []
for i in range(n):
    s,p = input().split()
    p = int(p)
    sp_list.append([s,-p,i+1])
    
sp_list = sorted(sp_list)
for s,p,i in sp_list:
    print(i)
