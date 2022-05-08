w = int(input())
n,k = map(int,input().split())
a_list =[]
b_list =[]

for i in range(n):
    a,b = map(int,input().split())
    a_list.append(a)
    b_list.append(b)

dp = [[0]*(w+1) for _ in range(n+1)]

for k in range(n):
    i = n-1-k
    for j in range(w+1):
        if j < a_list[i]:
            dp[i][j] = dp[i+1][j]
        else:
            dp[i][j] = max(dp[i+1][j],dp[i+1][j-a_list[i]]+b_list[i]) 
dp = sorted(dp,reverse=True) 
ans =0
print(dp)
for i in range(1,k):
    ans = max(ans,max(dp[i]))

print(ans) 
        
