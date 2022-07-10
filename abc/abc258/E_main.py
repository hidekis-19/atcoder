x = 24
ans = 0
for i in range(30):
    ans += ans*0.05
    ans += x
    print(i,int(ans))
