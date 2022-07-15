n = int(input())
k = int(input())
X = list(map(int,input().split()))

ans = 0

for x in X:
    a = x*2
    b = (k -x)*2
    ans += min(a,b)
print(ans)