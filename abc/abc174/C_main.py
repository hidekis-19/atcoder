k = int(input())

s = 0
for i in  range(1,1000000+1):
    s *= 10
    s += 7
    s %= k
    if s == 0:
        print(i)
        exit()

print(-1)    


