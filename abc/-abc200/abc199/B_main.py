N = int(input())
A = list(map(int, input().split())) 
B = list(map(int, input().split())) 
x = []
ans = ''
for i,a in enumerate(A):
    xi = list(range(a,B[i]+1,1))
    x.append(xi)

if N == 1:
    ans = set(x[0])
else:
    for j in range(N-1):
        if j >0:
            ans = set(x[j]) & set(x[j+1]) & set(ans) 
        else:
            ans = set(x[j]) & set(x[j+1])

print(len(list(ans)))
