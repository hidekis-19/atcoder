from itertools import permutations
N = int(input())
P = list(map(int, input().split())) 
Q = list(map(int, input().split())) 
n_list = list(range(1,N+1))

a = 0
b = 0

per=permutations(n_list,N)
for i,s in enumerate(per):
    if list(s) == P:
        a = i
    if list(s) == Q:
        b = i
print(abs(a-b))

