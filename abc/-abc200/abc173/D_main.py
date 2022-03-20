from collections import deque
n = int(input())

A = list(map(int, input().split())) 
B = deque()

ans = 0
while A:
    a = max(A)
    b = min(A)
    B.append(a)
    B.append(b)
    A.remove(a)
    A.remove(b)

B.append(B[0])
B.append(B[-1])

print(B)
for i in range(1,n-1):
    ans += min(B[i-1],B[i+1])
print(ans)


