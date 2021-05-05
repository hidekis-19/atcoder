N = input()
x =  '0'

ans = ''

def ispalindrome(str): return 1 if str == str[::-1] else 0

if ispalindrome(N) == 1:
    ans = 'Yes'
elif '0' not in N:
    ans = 'No'
else:
    for i in range(len(N)):
        N = str(x + N)
        if ispalindrome(N) == 1:
            ans = 'Yes'

if ans == '':
    ans = 'No'

print(ans)