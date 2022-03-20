N = int(input())
A = list(map(int, input().split())) 

ans = 0
b = 0
for k in range(2,max(A)+1):
    t = 0
    for a in A:
        if a%k==0:
            t += 1
    if t>=ans:
        ans = t
        b = k

print(b)

