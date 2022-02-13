n = int(input())


for i in range(1000):
    x = 2**i
    if x > n:
        print(i-1)
        exit()