l,h = map(int,input().split())
n = int(input())
A = []
for i in range(n):
    A.append(int(input()))
    

for a in A:
    if l <= a <= h:
        print(0)
    elif a < l:
        print(l-a)
    elif a > h:
        print(-1)
    