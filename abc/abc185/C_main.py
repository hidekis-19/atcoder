import itertools
L = int(input())

a = range(L-11,L)
b = range(1,12)
x = 1
y = 1

for i  in a:
    x = x*i

for i in b:
    y = y*i

print(x//y)


