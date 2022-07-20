a = int(input())
ans = 0
for i in range(1,a):
    x = i*(a-i)
    ans = max(ans,x)
print(ans)
    
    