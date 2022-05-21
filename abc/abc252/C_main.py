n = int(input())
s_list = []

for i in range(n):
    s_list.append(input())
    
ans = 99999999999999999999

t_list = []
for i in range(10):
    index_list = []
    for s in s_list:
        index_list.append(s.index(str(i)))
    
    index_list = sorted(index_list)
    t = index_list[0]
    a = index_list[0]
    index_list.pop(0)
    while index_list:
        if a != index_list[0]:
            t += index_list[0] -a 
            a = index_list[0]
            index_list.pop(0)
        else:
            index_list.append(index_list[0]+10)
            index_list.pop(0)
    t_list.append(t)
print(min(t_list))
