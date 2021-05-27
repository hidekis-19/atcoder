h,w = map(int,input().split())
S = []
for i in range(h):
    S.append(list(input()))

for i,s in enumerate(S):
    for j,t in enumerate(s):
        if t== '#':
            if i==0:
                if j==0 :
                    if (s[j+1] == '.' and  S[i+1][j] == '.'):
                        print('No')
                        exit()
                elif j == w-1:
                    if (s[j-1] == '.' and  S[i+1][j] == '.'):
                        print('No')
                        exit()
                else:
                    if (s[j-1] == '.' and s[j+1] == '.' and   S[i+1][j] == '.'):
                        print('No')
                        exit()
            elif i==h-1:
                if j==0:
                   if (s[j+1] == '.' and S[i-1][j] == '.' ):
                        print('No')
                        exit()
                elif j== w-1:
                   if (s[j-1] == '.' and S[i-1][j] == '.' ):
                        print('No')
                        exit()
                else:
                    if (s[j-1] == '.' and s[j+1] == '.' and   S[i-1][j] =='.'):
                        print('No')
                        exit()
            else:
                if j==0:
                    if (s[j+1] == '.' and S[i-1][j] == '.' and  S[i+1][j] == '.'):
                        print('No')
                        exit()
                elif j==w-1:
                    if (s[j-1] == '.' and S[i-1][j] == '.' and  S[i+1][j] == '.'):
                        print('No')
                        exit()
                else:
                    if (s[j-1] == '.' and s[j+1] == '.' and S[i-1][j] == '.' and  S[i+1][j] == '.'):
                        print('No')
                        exit()


print('Yes')

