N = int(input())

ans = 0
for i in range(N):
    a,b= map(int, input().split())
    x = 0
    y = 0
    x = int((a-1)*a*0.5)
    y = int(b*(b+1)*0.5)
    ans += y -x
print(ans)


