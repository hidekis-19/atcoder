n = int(input())
A =[]
B =[]

for i in range(n):
  A.append(list(map(int,input().split())))

m = int(input())
for i in range(m):
  B.append(list(map(int,input().split())))

A = sorted(A)
B = sorted(B)

for b in B:
  x = b[0] - A[0][0]
  y = b[1] - A[0][1]
  e = 0
  for i in range(1,n):
    s = A[i][0] +x
    t = A[i][1] +y
    if not [s,t] in B:
      e = 1
  if e==0:
    print(x,y)
    exit()
    