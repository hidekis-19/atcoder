n = int(input())
P = list(map(int,input().split()))
         
ans =0

for i in range(1,n-1):
    p1 = P[i-1]
    p2 = P[i]
    p3 = P[i+1]
    if p1 <= p2 <= p3:
        ans +=1
    elif p3 <= p2 <= p1:
        ans +=1
print(ans)
