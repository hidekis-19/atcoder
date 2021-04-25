N = int(input())
S = input()
Q = int(input())
Sl = list(S)

num_list = []
for i in range(Q):
    num_list.append(list(map(int,input().split())))


for j in num_list:
    t = j[0]
    a = j[1] -1
    b = j[2] -1
    if t == 1:
        x = Sl[a]
        Sl[a] = Sl[b]
        Sl[b] = x
    elif t == 2:
        x = Sl[:N]
        y = Sl[N:]
        Sl = y + x
print(''.join(Sl))
