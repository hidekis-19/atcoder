s = input()

for i in range(1,len(s)):
    if len(s[:len(s)-i])%2 ==0 and  s[:(len(s)-i)//2] + s[:(len(s)-i)//2] == s[:(len(s)-i)]:
        print(len(s[:len(s)-i]))
        exit()


