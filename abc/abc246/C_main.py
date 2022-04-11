n,k,x= map(int, input().split())
A = list(map(int, input().split())) 


B = []
A = sorted(A,reverse=True)
for i,a in enumerate(A) :
    if a >=x:
        B.append(a- x*(a//x))
        k = k - a//x
    else:
        B.append(A[i+1:])
        exit()
print(A)
B = sorted(B,reverse=True)
print(B)

if k ==0:
    print(sum(B))
else:
    print(sum( B[k-1:]))
            
    
    
