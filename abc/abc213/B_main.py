n = int(input())
A = list(map(int,input().split()))

B = []

for i,a in enumerate(A):
    B.append([a,i])
B = sorted(B,reverse=True)
print(B[1][1]+1)