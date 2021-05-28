a,b = map(int,input().split())
x = 1

if b==1:
    print(0)
    exit()

for i in range(1,100000):
    x += a -1
    if x >=b:
        print(i)
        exit()
