n,m = map(int,input().split())
s_list = list(map(str,input().split()))
t_list = set(map(str,input().split()))

    
for s in s_list:
    if s in t_list:
        print("Yes")
    else:
        print("No")