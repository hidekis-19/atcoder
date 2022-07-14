n,m,c = map(int,input().split())
B = list(map(int,input().split()))
A = []

for i in range(n):
    A.append(list(map(int,input().split())))

ans =0    

for a in A:
    s =0 
    for i,aa in enumerate(a):
        s += aa * B[i]
    if s +c >0 :
        ans += 1
print(ans)
        
            
