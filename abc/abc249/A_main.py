a,b,c,d,e,f,x = map(int,input().split())

taka = 0
aoki = 0

xx = x
yy = x

while xx > 0:
    if xx >= a:
        taka += + a*b
        xx -= a
    else:
        taka += xx*b
        xx -= xx
    xx -= c
while yy > 0:
    if yy >= c:
        aoki += + d*e
        yy -= d
    else:
        aoki += yy*e
        yy -= yy
    yy -= f


if taka > aoki:
    print("Takahashi")
elif taka < aoki:
    print("Aoki")
else:
    print("Draw")

