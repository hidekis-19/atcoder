n = int(input())
st_list = []
a =1 
for i in range(n):
    s,t = map(str,input().split())
    st_list.append([s,t])
    
for i,st in enumerate(st_list):
    s1 =st[0]
    for j,st2 in enumerate(st_list):
        s2 =st2[0]
        t2 =st2[1]
        if i != j:
            if (s1 != s2) and (s1 != t2):
                continue
            else:
                a =2
                

for i,st in enumerate(st_list):
    t1 =st[1]
    for j,st2 in enumerate(st_list):
        s2 =st2[0]
        t2 =st2[1]
        if i != j:
            if (t1 != s2) and (t1 != t2):
                continue
            elif a==2:
                print("No")
                exit()

print("Yes")
            
    
