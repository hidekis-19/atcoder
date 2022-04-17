A = list(map(int, input().split())) 

x = A[0]

for i in range(2):
    y = A[x]
    x = y
print(x)
