k = int(input())
a,b= map(int, input().split())

l = range(a,b+1)
ans = 'NG'
for a in l:
    if a%k==0:
        ans = 'OK'

print(ans)

