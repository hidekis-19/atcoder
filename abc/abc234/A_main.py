x = int(input())


def funcx (x):
    return x**2 + 2*x + 3

ans = funcx(funcx(funcx(x)+x)+ funcx(funcx(x)))
print(ans)

    