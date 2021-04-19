S = input()

ans_l = []
ans = []

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
        z = 1
        for j in range(len(ans_l)):
            x = 0
            if i+j+1 < len(ans_l):
                x = ans_l[i+j+1] - ans_l[i+j]
            if x == 1:
                z += 1
            else:
                break
        ans.append(z)
        
elif len(ans_l) == 1:
    ans.append(1)
else:
    ans.append(0)

print(max(ans))