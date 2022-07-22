s = input()

t = s[0]

if len(s) == 1:
    print(t.upper())
else:
    u = s[1:]
    print(t.upper() + u.lower())