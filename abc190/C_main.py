import itertools
n,m= map(int, input().split())

ans = 0

cond = [tuple(map(int, input().split())) for i in range(m)]

k = int(input())

num_list2 = []
for i in range(k):
    num_list2.append(list(map(int,input().split())))

for s in itertools.product(*num_list2):
    s = set(s)
    cnt = sum(A in s and B in s for A, B in cond)
    if ans < cnt:
        ans = cnt

print(ans)
    

            

