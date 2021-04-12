S = input()

ans_l = []
ans = 0

for i in range(len(S)):
    A = S.find('A',i)
    C = S.find('C',i)
    G = S.find('G',i)
    T = S.find('T',i)
    if A >=0:
        ans_l.append(A)
    if C>=0:
        ans_l.append(C)
    if G>=0:
        ans_l.append(G)
    if T>=0:
        ans_l.append(T)

ans_l = sorted(set(ans_l))

if len(ans_l) >=2:
    for i in range(len(ans_l)):
        ans = 1
        z = 1
        for j in range(len(ans_l)):
            x = ans_l[i+j+1] - ans_l[i+j]
            if x == 1:
                z += 1
        if z >= ans:
            ans = z
        
elif len(ans_l) == 1:
    ans = 1



print(ans)