a,b,c = map(int,input().split())

for i in range(1,110):
    x = a*i
    if x%b ==c:
        print("YES")
        exit()
print("NO")