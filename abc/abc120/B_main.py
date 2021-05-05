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

A,B,K= map(int, input().split())

A_div = make_divisors(A)
B_div = make_divisors(B)

ans_list = []

for i in A_div:
    if i in B_div:
        ans_list.append(i)
ans_list = sorted(ans_list,reverse=True)
print(ans_list[K-1])

