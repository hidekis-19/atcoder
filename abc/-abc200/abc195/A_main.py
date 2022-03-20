a,b= map(int, input().split())

c =  b%a
if c == 0:
    ans = 'Yes'
else :
    ans = 'No'
print(ans)