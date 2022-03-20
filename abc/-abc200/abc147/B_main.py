s = input()

ans = 0
x = len(s)//2

for i in range(x):
    if s[i] != s[-(i+1)]:
        ans += 1
print(ans)