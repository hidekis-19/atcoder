def split_list(l, n):
    """
    リストをサブリストに分割する
    :param l: リスト
    :param n: サブリストの要素数
    :return: 
    """
    for idx in range(0, len(l), n):
        yield l[idx:idx + n]

n,m = map(int,input().split())
A =[]
B =[]
for i in range(2*n):
    A.append(input())
    B.append([0,i])

for i in range(m):
    C = list(split_list(B,2))
    for j,c in enumerate(C):
        s = A[c[0][1]][i]
        t = A[c[1][1]][i]
        if (s=="G" and t=="C") or (s=="C" and t=="P") or (s=="P" and t=="G") :
            B[2*j] = [B[2*j][0]+1,B[2*j][1]]
        elif (t=="G" and s=="C") or (t=="C" and s=="P") or (t=="P" and s=="G"):
            B[2*j+1] = [B[2*j+1][0] + 1,B[2*j+1][1]]
    B = sorted(B, key=lambda x:(-x[0],x[1]))
            
for b in B:
    print(b[1]+1)
