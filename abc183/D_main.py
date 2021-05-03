N,W= map(int, input().split())
ans = 'Yes'

for i in range(N):
    s,t,p= map(int, input().split())
    if p>W:
        ans = 'No'
        break
    else:
        for j in range(s,t):
            water[j] += p
        if max(water)>W:
            ans = 'No'
            break
print(ans)