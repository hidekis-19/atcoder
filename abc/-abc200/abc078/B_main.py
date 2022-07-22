x,y,z = map(int,input().split())

ans = 0
x = x-z
while x >0:
    x = x - (y +z)
    if x >= 0:
        ans +=1
    else:
        print(ans)
        exit()
print(ans)