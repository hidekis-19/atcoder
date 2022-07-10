h,w = map(int,input().split())
A = []

for i in range(h):
    A.append(list(map(int,input().split())))
    
cnt = 0
cnt2= 0
for i in range(h-1):
    for j in range(w-1):
        cnt2 +=1
        if A[i][j] + A[i+1][j+1] <= A[i+1][j] + A[i][j+1]:
            cnt +=1

if cnt == cnt2:
    print("Yes")
else:
    print("No")