N = int(input())

n_all = 10**N
n_0 = 10**N - 9**N
n_9 = 10**N - 9**N
n_09 = 8**N

ans = (-n_all + n_09 + n_0 + n_9)%1000000007

print(ans)