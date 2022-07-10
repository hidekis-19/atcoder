n,x = map(int,input().split())
ab_list = []
for i in range(n):
    a,b = map(int,input().split())
    ab_list.append([a,b])

a0 = ab_list[0][0]
b0 = ab_list[0][1]
ans_i = a0 + b0
ans = a0 + b0*x
for i,ab in enumerate(ab_list):
    a1 = ab[0]
    b1 = ab[1]
    if i >= 1 and x>i-1:
        if ans > ans_i + a1 + b1*(x-i):
            ans = ans_i + a1 + b1*(x-i)
        ans_i += a1 + b1
    
print(ans)
