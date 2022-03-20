N = int(input())
A = list(map(int, input().split())) 

b = 0
ans = 0
sum = 0
i_max = 0

for i in range(N):
    b += A[i]
    i_max = max(i_max,b)
    ans = max(ans,sum+i_max)
    sum+= b
print(ans)

