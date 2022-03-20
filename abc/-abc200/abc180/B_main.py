n = int(input())
X = list(map(int, input().split())) 

ans1 = 0
ans2 = 0
ans3 = 0


for x in X:
    ans1 += abs(x)
    ans2 += x**2
    ans3 = max(ans3,abs(x))

print(ans1)
print(ans2**0.5)
print(ans3)

