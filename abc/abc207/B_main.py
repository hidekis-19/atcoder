a,b,c,d = map(int,input().split())

ans = 0
x =a
y = 0


for i in range(1,1000000):
    x += b
    y +=c
    if x <= y*d:
        print(i)    
        exit()
print(-1)