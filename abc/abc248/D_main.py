import bisect
n = int(input())
A = list(map(int, input().split())) 
Q = int(input())
Q_list = []

suji_list = [[] for i in range(200001)]

for i in range(Q):
    Q_list.append(list(map(int,input().split())))

for i,a in enumerate(A):
    suji_list[a].extend([i])

for q in Q_list:
    l = q[0]-1
    r = q[1]-1
    x = q[2]
    L = suji_list[q[2]]
    s = bisect.bisect_left(L,l)
    t = bisect.bisect_right(L,r)
    print(t-s)
        