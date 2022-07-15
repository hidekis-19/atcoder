h,w = map(int,input().split())
S = []

for i in range(h):
    S.append(list(input()))
    
T = []
for i in range(h):
    t = []
    for j in range(w):
        if S[i][j] == "#":
            t.append("#")
            continue
        else:
            if i != 0:
                x1 = S[i-1][j]
            else:
                x1 = "."
            if i != h -1:
                x5 = S[i+1][j]
            else:
                x5 = "."
            if j != 0:
                x7 = S[i][j-1]
            else:
                x7 = "."
            if j != w-1:
                x3 = S[i][j+1]
            else:
                x3 = "."
            if i != 0 and j != 0:
                x8 = S[i-1][j-1]
            else:
                x8 = "."
            if i != h-1 and j != 0:
                x6 = S[i+1][j-1]
            else:
                x6 = "."
            if j != w-1 and i != 0:
                x2 = S[i-1][j+1]
            else:
                x2 = "."
            if j != w-1 and i != h-1:
                x4 = S[i+1][j+1]
            else:
                x4 = "."
        X = [x1,x2,x3,x4,x5,x6,x7,x8]
        t.append(X.count("#"))
    T.append(t)

for t in T:
    print("".join(map(str,t)))
        
        
        
