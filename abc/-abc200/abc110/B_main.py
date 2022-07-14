n,m,x,y = map(int,input().split())
X = list(map(int,input().split()))
Y = list(map(int,input().split()))

X = sorted(X)
Y = sorted(Y)

xx = max(X)
yy = min(Y)
ss =[]
for i in range(-100,101):
    if x < i and i <= y:
        ss.append(i)
for s in ss:
    if xx < s and s<= yy:
        print("No War")
        exit()

print("War")
