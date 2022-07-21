s = input()
n = int(input())

l = []

for i in list(s):
    for j in list(s):
        l.append(i +j)

print(l[n-1])
        
