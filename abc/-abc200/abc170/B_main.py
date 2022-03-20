x,y= map(int, input().split())


s = (4*x-y)%2
t = (y-2*x)%2
ss = (4*x-y)//2
tt = (y-2*x)//2

ans = 'No'
if s==0 and t==0 and ss>=0 and tt>=0:
    ans = 'Yes'

print(ans)