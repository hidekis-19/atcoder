N = int(input())
x_y = []
for i in range(N):
    v = list(map(int,input().split()))
    v1 = v[0]
    v2 = v[1]
    x_y.append([v[0],v[1],i])
S =input()


x_y_sorted =sorted(x_y, key=lambda x:(x[1],x[0]))
for i in range(N-1):
    if x_y_sorted[i][1] == x_y_sorted[i+1][1]:
        a = x_y_sorted[i][2]
        b = x_y_sorted[i+1][2]
        if S[a] =="R" and  S[b] == "L" :
            print("Yes")
            exit()

print("No")        
