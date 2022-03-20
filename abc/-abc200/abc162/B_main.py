N = int(input())
l = []
for n in range(1,N+1):
    if n%3==0 and n%5==0:
        continue
    elif n%3==0:
        continue
    elif n%5==0:
        continue
    else:
        l.append(n)
print(sum(l))



