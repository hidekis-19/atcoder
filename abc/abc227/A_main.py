n,k,a = map(int,input().split())

hito = list(range(1,n+1))

hito = hito[a-1:]+hito[:a-1]
cnt = 1
while True:
    for h in hito:
        if cnt == k:
            print(h)
            exit()
        cnt +=1    

