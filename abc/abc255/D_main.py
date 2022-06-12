import bisect
n,q = map(int,input().split())
A = list(map(int,input().split()))
x_list = []

for i in range(q):
    x_list.append(int(input()))

A = sorted(A)

su =0
sumA_list = []
for a in A:
    su += a
    sumA_list.append(su)
sumA = sum(A)    

for x in x_list:
    if x <= A[0]:
        print(sumA-n*x)
    elif x >=A[n-1]:
        print(n*x-sumA)
    else:
        b = bisect.bisect(A,x)
        print((2*b-n)*x-2*sumA_list[b-1]+sumA)
    
    
