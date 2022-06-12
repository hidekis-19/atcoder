x,a,d,n = map(int,input().split())

an = a + (n-1)*d

if x >= an and a <= an:
    print(x-an)
elif x <= a and a <= an :
    print(a-x)
elif x >= a and a > an :
    print(x-a)
elif x <= an and a > an :
    print(an-x)
else:
    y = x -a
    s = y//d
    t = y//d +1
    v = a + s*d
    u = a + t*d
    ans = min(abs(x-v),abs(x-u))
    print(ans) 
    