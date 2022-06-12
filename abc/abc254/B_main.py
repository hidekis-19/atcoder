n = int(input())

A = [[1]]

for i in range(2,n+1):
    s = [0]*i
    s[0] = 1
    s[i-1] = 1
    if i == 2:
        A.append(s)
    else:
        for j in range(1,i-1):
            s[j] = A[i-2][j-1] + A[i-2][j]
        A.append(s)

for a in A:
    print(' '.join(map(str,a)))
    
    