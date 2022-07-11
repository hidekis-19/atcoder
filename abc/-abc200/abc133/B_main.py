n,d = map(int,input().split())

X = []

for i in range(n):
    X.append(list(map(int,input().split())))

ans =0

for i in range(n-1):
    for j in range(i+1,n):
        x = 0
        for k in range(d):
            x += (X[i][k] -  X[j][k])**2
        
        y = x**0.5
        if y - int(y) ==0:
            ans +=1
print(ans)
                
