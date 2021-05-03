def main():

    S = input()
    Sl = list(range(len(S)))
    T = ''
    t = False
    for i in Sl:
        if S[i] == 'R':
            if t:
                t = False
            else:
                t = True
        elif not t:
            if len(T)>0 and  T[-1:] == S[i]:
                T = T[:-1]
            else :
                T = T + S[i]
        else:
            if len(T)>0 and T[0] == S[i]:
                T = T[1:]
            else:
                T = S[i] + T

    if  t:
        T = T[::-1]
    print(T)


main()


