n,k,x= map(int, input().split())
A = list(map(int, input().split())) 

while True:
    A = sorted(A,reverse=True)
    s = 0
    for i,a in enumerate(A):
        s = i
        if a < x:
            break
        elif a <= k*x:
            k = k - a//x 
            A[i] = a - (a//x)*x
        else :
            A[i] = a - k*x
            print(sum(A))
            exit()
    if s==0:
        break
print(sum(A[k:]))
