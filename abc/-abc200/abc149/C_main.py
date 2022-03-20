x = int(input())

if x==2:
    print(2)
    exit()

while True:
    y = int(x**0.5)+1
    t = 0
    s = len(list(range(2,y+1)))
    for i in range(2,y+1):
        if x %i>0:
            t += 1
    if s==t:
        print(x)
        break
    else:
        x +=1
            


