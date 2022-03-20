n = int(input())
A = list(map(int,input().split()))

t = 0
s = 0
for a in A:
    if a%2==0 and (a%3==0 or a%5==0):
        t += 1
    if a%2==0:
        s +=1


if t== s:
    print('APPROVED')
else:
    print('DENIED')










