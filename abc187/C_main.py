N = int(input())

S = set(input() for i in range(N))
ans = ''
ans_ng = 'satisfiable'

for s in S:
    if  '!' + s in S:
        print(s)
        exit()

print(ans_ng)

