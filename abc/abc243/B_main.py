N = int(input())
A = list(map(int, input().split())) 
B = list(map(int, input().split())) 

ans_1 =0
ans_2 =0

for i in range(len(A)):
    if A[i] == B[i]:
        ans_1 +=1
    elif  A[i] in B :
        ans_2 +=B.count(A[i])

print(ans_1)
print(ans_2)

        