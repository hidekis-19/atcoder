def main():
    N = int(input())
    S = input()
    Q = int(input())
    Sl = list(S)
    num_list =  [list(map(int, input().split())) for _ in range(Q)]
    t = False

    for j in num_list:
        if j[0] == 2:
            if t == False:
                t = True
            else:
                t = False
        if t:
            a = j[1]
            b = j[2]
            if a <= N:
                a = a+N
            else:
                a = a-N
            if b <= N:
                b = b+N
            else:
                b = b-N
            x = Sl[a-1]
            Sl[a-1] = Sl[b-1]
            Sl[b-1] = x
        else:
            x = Sl[j[1]-1]
            Sl[j[1]-1] = Sl[j[2]-1]
            Sl[j[2]-1] = x
    if t:
        Sl = Sl[N:]+Sl[:N]
    print(''.join(Sl))
main()