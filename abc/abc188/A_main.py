a,b= map(int, input().split())

ans = 'No'

if abs(a-b)<= 2:
    ans = 'Yes'

print(ans)