s= input()

moji = []

for i in range(len(s)):
    x = s[i:] + s[:i]  
    moji.append(x)
print(min(moji))
print(max(moji))