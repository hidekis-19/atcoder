x,y,a,b= map(int, input().split())
ans = -1
while x < y :
    x = min(x*a,x+b)
    print(x)
    ans += 1
print(ans)