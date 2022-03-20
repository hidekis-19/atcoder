A = []

for i in range(3):
    A.append(list(map(int,input().split())))

n = int(input())
B = []
for i in range(n):
    B.append(int(input()))


for i,a in enumerate(A):
    for b in B:
        if a.count(b):
            A[i][a.index(b)] = '#'

#yoko
ans = 'No'
s = 0
t = 0
u = 0
for a in A:
    if a.count('#') ==3:
        ans = 'Yes'
    if a[0] == '#':
        s +=1
    if a[1] == '#':
        t += 1
    if a[2] == '#':
        u += 1

if s==3 or t == 3 or u ==3:
    ans = 'Yes'

if A[0][0] =='#' and A[1][1] == '#' and A[2][2] == '#':
    ans ='Yes'
if A[0][2] =='#' and A[1][1] == '#' and A[2][0] == '#':
    ans ='Yes'

print(ans)


