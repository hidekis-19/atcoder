from collections import deque
N,M= map(int, input().split())
ans = 0
if M==0:
    print(1)
elif N==M:
    print(0)
else:
    A = list(map(int, input().split())) 
    k = 99999999999999
    A = sorted(A)
    d = deque()

    for i in range(M-1):
        if A[i+1]-A[i] >= 2:
            k = min(k,A[i+1]-A[i]-1)
            d.append(A[i+1]-A[i]-1)
    if A[0] !=1:
        d.appendleft(A[0]-1)
        k = min(k,A[0]-1)
    if A[-1] !=N:
        d.append(N- A[-1]) 
        k = min(k,N - A[-1])
    for b in d:
        if b%k==0:
            ans += b//k
        else:
            ans += b//k+1
    print(ans)






