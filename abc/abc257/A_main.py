n,x = map(int,input().split())

a = [chr(i) for i in range(65,65+26)]

b = ""

for i in a:
    for j in range(n):
        b = b + i 

print(b[x-1])

