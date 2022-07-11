from itertools import combinations

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
k = int(input())

s = [a,b,c,d,e]

base = list(combinations(s,2))

for x,y in base:
    if abs(x-y) >k:
        print(":(")
        exit()
print("Yay!")
        