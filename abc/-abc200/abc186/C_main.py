N = int(input())

n_list = range(1,N+1)

ans = 0
for n in n_list:
    n8 = oct(n)
    if not( ('7' in str(n8) ) or ('7' in str(n))):
        ans +=1
print(ans)
