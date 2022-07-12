s = int(input())

se = {s}

cnt =1
while True:
    cnt +=1
    if s%2 == 0:
        s = s//2
    else:
        s = 3*s+1
    if s in se:
        print(cnt)
        exit()
    se.add(s)
