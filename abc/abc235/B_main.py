n = int(input())
h_list = list(map(int,input().split()))

ans = 0

for h in h_list:
    if ans < h:
        ans =h
    else:
        print(ans)
        exit()    

print(ans)