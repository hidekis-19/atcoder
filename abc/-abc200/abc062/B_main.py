h,w = map(int,input().split())
A = []

for i in range(h):
    A.append(input())
    
B = []

for a in A:
    x = "#" + a + "#"
    B.append(x)

print("#"*(w+2))
for b in B:
    print(b)
print("#"*(w+2))
    
