import itertools
N = int(input())
S = input()

num = ['0','1','2','3','4','5','6','7','8','9']
ans = 0

for i in num:
    cnt = 0
    S_l = list(S)
    if i in S_l:
        n1 = S_l.index(i)
        for k in  num:
            if k in S_l[int(n1)+1:]:
                n2 = S_l[int(n1)+1:].index(k)
                for j in  num:
                    if (j in S_l[int(n1+n2)+2:]) :
                        ans += 1
            
print(ans)



