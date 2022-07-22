a,b = map(str,input().split())

c = int(a+b)

for i in range(1,2000):
    if c == i**2:
        print("Yes")
        exit()
print("No")
