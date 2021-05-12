n = int(input())

A = list(map(int, input().split())) 
B = [n%200 for n in A]

ans = 0
for i in range(0,200):
    ans += B.count(i)*(B.count(i)-1)/2
print(int(ans))
