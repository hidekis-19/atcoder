n = int(input())

l = []

if n >=8:
    n -= 8
    l.append(8)
if n>=4:
    n -= 4
    l.append(4)
if n>=2:
    n -= 2
    l.append(2)
if n>=1:
    n -= 1
    l.append(1)
print(len(l))

for i in l:
    print(i)
    
    