a,b,x = map(int,input().split())

if x <a:
    print("NO")
elif b >= x-a:
    print("YES")
else:
    print("NO")
