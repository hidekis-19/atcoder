h = int(input())

ans = 0
s = 1
while True:
    if h==1:
        ans += s
        print(ans)
        break
    else:
        ans += s
        s *= 2
        h = h//2

    