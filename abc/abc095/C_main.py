A,B,C,X,Y= map(int, input().split())
ans = []

ans.append(C*2*max(X,Y))
if X <= Y:
    y = Y -X
    ans.append(C*X*2 + B*y)
else :
    x = X -Y
    ans.append( C*Y*2 + A*x)
ans.append(A*X + B*Y)

print(min(ans))
    