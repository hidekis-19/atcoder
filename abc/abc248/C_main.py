n, m, K = list(map(int, input().split()))
dp = [[0]*(K+1) for _ in range(n+1)]
dp[0][0] = 1

for i in range(n):
    for j in range(K):
        for k in range(1, m+1):
            if (j+k<=K): 
                dp[i+1][j+k] +=  dp[i][j]
print(sum(dp[n]) % 998244353)