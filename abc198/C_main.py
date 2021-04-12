R,X,Y= map(int, input().split())

ans = 0

dis = (X**2 + Y**2)**0.5
r = R

if dis == r:
    ans = 1
elif (dis> r) and (dis%r == 0):
    ans = int(dis/r)
elif dis < r:
    ans = 2
else:
    ans = int(dis/r) + 1


print(ans)


