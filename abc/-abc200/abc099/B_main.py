a,b = map(int,input().split())

def su(n):
    nn = n*(n+1)//2
    return nn

def my_index(l, x, default=False):
    if x in l:
        return l.index(x)
    else:
        return False

numList = []

for i in range(1,1000):
    numList.append(su(i))


for i in range(1,499500):
    if my_index(numList,a+i) and my_index(numList,b+i):
        x = my_index(numList,a+i)
        y = my_index(numList,b+i)
        if y-x ==1:
            print(i)
            exit()
        