n = int(input())
log_list = [0]*200010

for i in range(n):
    l,r = map(int,input().split())
    log_list[l] += 1
    log_list[r] -= 1

for i in range(1,200005):
    log_list[i] += log_list[i-1]
    
    
f = False
for i,log in enumerate(log_list):
    if log >= 1 and not f:
        ll = i
        f = True        
    elif log == 0 and f:
        print(ll,i)
        f = False
    

