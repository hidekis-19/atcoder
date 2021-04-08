import sys
H,W,X,Y= map(int, input().split())

S = [[c for c in l.strip()] for l in sys.stdin]
x_left = X-2
x_right = X
y = X-1
ans = 0
l = S[y]

x = Y-1
y_top = X-2
y_under = X

if S[y][x] == '.':
    ans += 1

while x_left >= 0:
    a = l[x_left]
    if a == '.':
        ans += 1
    x_left -= 1

while x_right < W:
    a = l[x_right]
    if a == '.':
        ans += 1
    x_right += 1


while y_top >= 0:
    ll =  S[y_top]
    a = ll[x]
    if a == '.':
        ans += 1
    y_top -= 1


while y_under < H:
    ll = S[y_under]
    a = ll[x]
    if a == '.':
        ans += 1
    y_under += 1


print(ans)



