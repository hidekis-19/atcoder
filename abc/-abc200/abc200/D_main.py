n = int(input())

A = list(map(int, input().split())) 
B =[]
C =[]



for i in range(n):
    for j in range(i+1,n+1):
        B.append([i,j])
        C.append(sum(A[i:j])%200)


aaa = 0

for j in range(201):
    aa = [i for i,x in enumerate(C) if x == j]
    if len(aa)>=2 :
        b = B[aa[0]]
        c = B[aa[1]]
        x = list(range(b[0]+1,b[1]+1))       
        y = list(range(c[0]+1,c[1]+1))   
        xx = " ".join([str(_) for _ in x])
        yy = " ".join([str(_) for _ in y])
        print('Yes')
        print(len(x),xx)
        print(len(y),yy)
        aaa = 1
        break
if aaa == 0:
    print('No')




