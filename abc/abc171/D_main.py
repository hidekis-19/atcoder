n = int(input())
A = list(map(int,input().split()))
Q = int(input())
bc_list = []
for i in range(Q):
    bc_list.append(list(map(int,input().split())))

A_list = [0]*1000000

sumA = sum(A)

for a in A:
    A_list[a-1] += 1

for i in bc_list:
    b = i[0]
    c = i[1]
    x = A_list[b-1]
    A_list[c-1] += x
    A_list[b-1] = 0
    sumA = sumA + (c-b)*x
    print(sumA)




