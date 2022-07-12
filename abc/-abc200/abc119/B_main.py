n = int(input())
xuList = []
for i in range(n):
    x,u = input().split()
    x = float(x)
    xuList.append([x,u])

yen = 380000

ans = 0

for x,u in  xuList:
    if u == "JPY":
        ans += x
    elif u == "BTC":
        ans += x*yen
print(ans)
    
    

    
