n = int(input())
A = list(map(int, input().split())) 


ans = 0
x =0
for i in range(len(A)-1):
    if A[i] > A[i+1]:
        ans += A[i]-A[i+1]
        A[i+1] = A[i]
print(ans)
