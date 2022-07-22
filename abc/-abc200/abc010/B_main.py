n = int(input())
A = list(map(int,input().split()))

ans = 0

for a in A:
    if (a+1)%3 == 0 or a%2 == 0:
        for i in range(1,10):
            if (a+1-i)%3 != 0 and (a-i)%2 != 0:
                ans += i
                break
print(ans)