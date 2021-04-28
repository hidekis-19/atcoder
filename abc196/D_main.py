H,W,A,B= map(int, input().split())

ans = 0

S = H*W

for b in range(1,S):
    if ((S-b)%2*A==0) and ((S-b)/2*A>0):
        ans +=1

print(ans)
    
