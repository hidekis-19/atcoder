n,k= map(int, input().split())
A = list(map(int, input().split())) 
B = list(map(int, input().split())) 
s = [A[0],B[0]]

for i in range(n-1):
    x = []
    t = [A[i+1],B[i+1]]
    if abs(s[0]-t[0]) <= k:
        x.append(t[0])
    if abs(s[0]-t[1]) <= k:
        x.append(t[1])
    elif len(s) ==2:
        if abs(s[1]-t[0]) <= k:
            x.append(t[0])
        if abs(s[1]-t[1]) <= k:
            x.append(t[1])
    if len(x) == 0:
        print("No")
        exit()
    s = list(set(x))

print("Yes")
    
    
    
    
    

