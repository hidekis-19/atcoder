s = input()
t = input()

for i in range(len(s)):
    if s[i] == t[i] or (s[i] == "@" and t[i] in ["a","t","c","o","d","e","r"] )or (t[i] == "@" and s[i] in ["a","t","c","o","d","e","r"]):
        continue
    else:
        print("You will lose")
        exit()
print("You can win")            