n = int(input())
A = list(map(int,input().split()))
X = int(input())

sumA = sum(A)
lenA = len(A)
ans = 1

s = X // sumA
ans += lenA * s
X = X % sumA

for a in A:
    if a <=X:
        ans += 1
        X -= a
    else:
        print(ans)
        exit()
    
