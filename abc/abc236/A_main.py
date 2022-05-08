S = input()
a,b = map(int,input().split())

S = list(S)

x = S[a-1]
y = S[b-1]

S[a-1] = y
S[b-1] = x
print("".join(S))