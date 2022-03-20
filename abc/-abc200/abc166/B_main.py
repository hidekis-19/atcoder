n,k= map(int, input().split())

ans = [0]*n
for i in range(k):
    d = int(input())
    A = list(map(int, input().split())) 
    for a in A:
        ans[a-1] += 1
print(ans.count(0))
    