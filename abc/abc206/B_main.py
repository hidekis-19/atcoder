n = int(input())
x = 0
for i in range(1,1000000):
    x +=i
    if x >=n:
        print(i)
        exit()



    