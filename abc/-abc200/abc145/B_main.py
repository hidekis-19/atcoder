n = int(input())
s = input()

ans = 'No'

if s == s[:n//2] + s[n//2:] and s[:n//2] == s[n//2:]:
    ans = 'Yes'
print(ans)