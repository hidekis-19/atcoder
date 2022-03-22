n = int(input())

l = list(range(1,2*n+2))
for i in range(2*n+2):
    print(l[0])
    l.pop(0)
    x = int(input())
    if x ==0:
        exit()
    l.remove(x)
        