n = int(input())
A = []

for i in range(n):
    A.append(int(input()))

ri = [0]*100005

ans = 1
ins = A[0] -1

if A[0] ==2:
    print(1)
    exit()
while True:
    t = A[ins]    
    ans += 1
    if t == 2:
        print(ans)
        exit()
    ins = t -1
    if ri[ins] ==1:
        print("-1")
        exit()
    ri[ins] = 1    
        