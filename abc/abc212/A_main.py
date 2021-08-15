a,b = map(int,input().split())

x = 'Gold'
y = 'Silver'
z = 'Alloy'

if a > 0 and b== 0:
    print(x)
elif a==0 and b> 0:
    print(y)
elif a>0 and b>0:
    print(z)

