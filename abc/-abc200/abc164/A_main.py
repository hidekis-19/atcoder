s,w = map(int,input().split())

ans = 'safe'

if w>=s:
    ans = 'unsafe'
print(ans)