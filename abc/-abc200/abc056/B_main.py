w,a,b = map(int,input().split())

if a <= b:
    if w >= b-a:
        print(0)
    else:
        print(b-w-a)
else:
    if w >= a-b:
        print(0)
    else:
        print(a-w-b)
        
