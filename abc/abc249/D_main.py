import collections
import collections
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

n = int(input())
A = map(int,input().split())

C = collections.Counter(A)

ans = 0
for i in C.keys():
    X = make_divisors(i)
    for x in X:
        ans += C[i]*C[x]*C[i/x]
print(ans)