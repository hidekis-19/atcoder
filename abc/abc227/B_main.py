n = int(input())
S = list(map(int,input().split()))

menseki= set()

for a in range(1,1000):
    for b in range(1,1000):
        x = 4*a*b + 3*a +3*b
        if 1<= x <=1000:
            menseki.add(x)

        
ans = 0

for s in S:
    if s not in menseki:
        ans += 1
print(ans)
        

