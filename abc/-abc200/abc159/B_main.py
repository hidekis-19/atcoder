def ispalindrome(str): return 1 if str == str[::-1] else 0

s = input()
n = len(s)
t = s[:int((n-1)/2)]
u = s[int((n+3)/2-1):]


if ispalindrome(s) and  ispalindrome(t) and ispalindrome(u):
    print('Yes')
else:
    print('No')