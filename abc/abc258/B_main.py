n = int(input())
A = []
B = []

for i in range(n):
    z= list(input())
    x = [int(s) for s in z]
    A.append(x)
    y = x + x + x
    B.append(y)

C = B + B + B

frs_val = 0    
frs_i = []
frs_j = []

for i in range(n):
    for j in range(n):
        x = A[i][j]
        if frs_val < x:
            frs_val = x
            frs_i = []
            frs_j = []
            frs_i.append(i)
            frs_j.append(j)
        elif frs_val == x:
            frs_i.append(i)
            frs_j.append(j)

ans = str(frs_val)
aa = []
for v in range(min(len(frs_i),n)):
    ans_l = [ans]*8
    ii = frs_i[v] + n
    jj = frs_j[v] + n
    t1=t2=t3=t4=t5=t6=t7=t8 = 0
    for i in range(1,n):
        t1 = C[ii][jj-i]
        s = C[ii][jj]
        t5 = C[ii][jj+i]
        t8 = C[ii-i][jj-i]
        t7 = C[ii-i][jj]
        t6 = C[ii-i][jj+i]
        t2 = C[ii+i][jj-i]
        t3 = C[ii+i][jj]
        t4 = C[ii+i][jj+i]
        T = [t1,t2,t3,t4,t5,t6,t7,t8]
        for k,t in enumerate(T):
            ans_l[k] = ans_l[k] + str(t)

    lll = [int(s) for s in ans_l]
    aa.append(max(lll))
print(max(aa))