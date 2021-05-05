from collections import Counter
ans = 'No'
n = input()
eights = range(112,1000,8)

n_cnt = Counter(n)

if len(n)==1 and n == '8':
    ans = 'Yes'
elif len(n) == 2:
    if int(n)%8==0:
        ans = 'Yes'
    else :
        n = int(n[1] + n[0])
        if n%8==0:
            ans = 'Yes'
else:
    for i in eights:
        if not Counter(str(i)) - n_cnt :
            ans = 'Yes'
print(ans)

