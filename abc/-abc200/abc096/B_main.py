a,b,c = map(int,input().split())
k = int(input())

l = [a,b,c]

for i in range(k):
    l = sorted(l)
    x = l.pop()
    y = 2*x
    l.append(y)

print(sum(l))