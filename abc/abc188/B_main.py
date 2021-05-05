n = int(input())

a = list(map(int, input().split())) 
b = list(map(int, input().split())) 

ans = 0
ans_n = 'No'
for i,aa in enumerate(a):
    ans += aa*b[i]


if ans ==0:
    ans_n = 'Yes'

print(ans_n)