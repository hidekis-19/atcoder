import collections
n = int(input())
A = list(map(int,input().split()))

c = collections.Counter(A)


ans = 0
for i in range(n-1):
    x = c[A[i]] -1
    ans += n - (i+1) -x
    c[A[i]] = x 
print(ans)



