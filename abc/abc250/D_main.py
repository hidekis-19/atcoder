import bisect
n = int(input())
s_list = []

for i in range(2,int(n**(1/3)+1)+1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        s_list.append(i)

ans = 0
for s in s_list:
    x = int(n //(s**3))
    y = s_list.index(s)
    print(s**3,x,s_list[:y])
    ans+= bisect.bisect(s_list[:y],x)
print(ans)
