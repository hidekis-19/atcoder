x = int(input())
a = 100
for i in range(1,1000001):
    a +=  int(a//100)
    if a >= x:
        print(i)
        exit()