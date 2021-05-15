N = int(input())
S = []
T = []
for i in range(N):
    s,t= input().split()
    S.append(s)
    T.append(int(t))

U = sorted(T,reverse=True)


ans = S[T.index(U[1])]

print(ans)

