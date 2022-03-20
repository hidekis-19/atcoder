n = int(input())
A = list(map(int,input().split()))

X = [0]*1000000

for a in A:
    X[a-1] += 1

ans = 0

for i,x in enumerate(X):
    if i == 0:
        ans = max(ans,X[i]+X[i+1])
    elif i==len(X)-1:
        ans = max(ans,X[i-1]+X[i])
    else:
        ans = max(ans,X[i-1]+X[i]+X[i+1])
print(ans)