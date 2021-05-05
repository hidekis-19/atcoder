def main():
    from collections import deque
    S = input()
    T = deque()
    t = True
    for i in range(len(S)):
        if S[i] == 'R':
            if t:
                t = False
            else:
                t = True
        elif not t:
            if T and  T[-1] == S[i]:
                T.pop()
            else :
                T.append(S[i])
        else:
            if T and T[0] == S[i]:
                T.popleft()
            else:
                T.appendleft(S[i])

    if  t:
        T = reversed(T)
    print(''.join(T))


main()


