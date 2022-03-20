x,n= map(int, input().split())

p = list(map(int, input().split())) 


l = list(range(200))

ans = 0
y = 10000
for i in l:
    if i  in p:
        continue
    if y > abs(x-i):
        y = abs(x-i)
        ans = i

print(ans)