S = input()

ans = ''
for s in (reversed(S)):
    if s == '6':
        s ='9'
    elif s == '9':
        s = '6'
    ans = ans+s
print(ans)

