N = int(input())

num_list = list(range(2,N+1,1))
num_list_2 = []

for i in num_list:
    y = 2
    while i ** y <= N:
        num_list_2.append(i**y)
        y += 1

ans = N - int(len(set(num_list_2)))

print(ans)


