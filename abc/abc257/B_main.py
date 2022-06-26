n,k,q = map(int,input().split())
A = list(map(int,input().split()))
L = list(map(int,input().split()))



for l in L:
    if A[l-1] == n:
        continue
    else:
        if l == k and k <n:
            A[l-1] = A[l-1] + 1    
        elif A[l-1] +1 != A[l]:
            A[l-1] = A[l-1] + 1
print(' '.join(map(str,A)))
            

