N = int(input())

x = int(N**0.5) + 1
ans = 10000000000

for i in range(x):
    a = N / (i + 1)
    b = a - int(a)
    if b == 0:
        y = max(len(str(i+1)),len(str(int(a))))
    if y < ans:
        ans = y


print(ans)
