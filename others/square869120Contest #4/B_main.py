from statistics import median 
n = int(input())
A = []
B = []
X = []
for i in range(n):
  a,b = map(int,input().split())
  A.append(a)
  B.append(b)
  X.append([a,b])
	
s = 10000000000
t = 10000000000
x = min(A)
y = max(B)
c = int(median(A))
d = int(median(B))
for i in range(max(0,c-10000),c+10000):
  u = 0
  for a in A:
    u += abs(i-a)
  if s > u:
    x = i
    s = u
for i in range(max(0,d-10000),d+10000):
  v = 0
  for b in B:
    v += abs(i-b)
  if t > v:
    y = i
    t = v

ans = 0

for i in X:
  ans += abs(x-i[0]) +i[1] -i[0] +abs(y-i[1])
print(ans)  
    