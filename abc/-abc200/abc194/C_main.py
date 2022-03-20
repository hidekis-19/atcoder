N = int(input())
A =  list(map(int, input().split()))  # n個の数字がリストに格納される
 
ans = 0
ans1 = 0
ans2 = 0

for i in A:
    ans1 += i**2
ans += N*ans1

ans2 = sum(A)**2
ans -= ans2

print(ans)


