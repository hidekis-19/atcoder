n = int(input())

ans_v = set()
ans_p = -1
ans_i = 9999999999


st_list = []
for i in range(n):
    s,t = input().split()
    s = str(s)
    t = int(t)
    st_list.append([s,t])


for i,st in enumerate(st_list):
    s = st[0]
    t = st[1]
    if t > ans_p and s not in ans_v :
        ans_i = i
        ans_p = t
    ans_v.add(s)
print(ans_i+1)    

