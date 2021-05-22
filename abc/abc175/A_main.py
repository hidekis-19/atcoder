s = input()

c = s.count('R')

if c ==0:
    ans = 0
elif c == 1:
    ans =1
elif c==2:
    if not s[1] =='S':
        ans = 2
    else:
        ans =1
else:
    ans = 3 

print(ans)