x,k,d= map(int, input().split())


if abs(x) >= k*d:
    x = abs(x) -d*k
else:
    y = abs(x)//d
    x = abs(x) - d*y
    k = k-y
    if k%2!=0:
        x = abs(x-d)

print(x)        
