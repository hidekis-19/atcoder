n = int(input())
S = []

for i in range(n):
    S.append(list(input()))
    
T = [["" for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):

        if i <= n//2 and j <= n//2:
            T[j][n-1-i] = S[i][j]
        elif i <= n//2 and j >= n//2:
            T[j][n-1-i] = S[i][j]
        elif i >= n//2 and j <= n//2:
            T[j][i-n+1] = S[i][j]
        elif i >= n//2 and j >= n//2:
            T[j][i-n+1] = S[i][j]

for t in T:
    print("".join(t))
